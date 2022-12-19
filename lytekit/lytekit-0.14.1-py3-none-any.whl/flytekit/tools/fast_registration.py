from __future__ import annotations

import hashlib
import os
import posixpath
import subprocess as _subprocess
import tarfile
from typing import Optional

from flytekit.core.context_manager import FlyteContextManager
from flytekit.tools.ignore import DockerIgnore, GitIgnore, IgnoreGroup, StandardIgnore

FAST_PREFIX = "fast"
FAST_FILEENDING = ".tar.gz"

file_access = FlyteContextManager.current_context().file_access


def fast_package(source: os.PathLike, output_dir: os.PathLike) -> os.PathLike:
    """
    Takes a source directory and packages everything not covered by common ignores into a tarball
    named after a hexdigest of the included files.
    :param os.PathLike source:
    :param os.PathLike output_dir:
    :return os.PathLike:
    """
    ignore = IgnoreGroup(source, [GitIgnore, DockerIgnore, StandardIgnore])
    digest = compute_digest(source, ignore.is_ignored)
    archive_fname = f"{FAST_PREFIX}{digest}{FAST_FILEENDING}"

    if output_dir:
        archive_fname = os.path.join(output_dir, archive_fname)

    with tarfile.open(archive_fname, "w:gz") as tar:
        tar.add(source, arcname="", filter=ignore.tar_filter)

    return archive_fname


def compute_digest(source: os.PathLike, filter: Optional[callable] = None) -> str:
    """
    Walks the entirety of the source dir to compute a deterministic md5 hex digest of the dir contents.
    :param os.PathLike source:
    :param Ignore ignore:
    :return Text:
    """
    hasher = hashlib.md5()
    for root, _, files in os.walk(source, topdown=True):

        files.sort()

        for fname in files:
            abspath = os.path.join(root, fname)
            relpath = os.path.relpath(abspath, source)
            if filter:
                if filter(relpath):
                    continue

            _filehash_update(abspath, hasher)
            _pathhash_update(relpath, hasher)

    return hasher.hexdigest()


def _filehash_update(path: os.PathLike, hasher: hashlib._Hash) -> None:
    blocksize = 65536
    with open(path, "rb") as f:
        bytes = f.read(blocksize)
        while bytes:
            hasher.update(bytes)
            bytes = f.read(blocksize)


def _pathhash_update(path: os.PathLike, hasher: hashlib._Hash) -> None:
    path_list = path.split(os.sep)
    hasher.update("".join(path_list).encode("utf-8"))


def get_additional_distribution_loc(remote_location: str, identifier: str) -> str:
    """
    :param Text remote_location:
    :param Text identifier:
    :return Text:
    """
    return posixpath.join(remote_location, "{}.{}".format(identifier, "tar.gz"))


def download_distribution(additional_distribution: str, destination: str):
    """
    Downloads a remote code distribution and overwrites any local files.
    :param Text additional_distribution:
    :param os.PathLike destination:
    """
    file_access.get_data(additional_distribution, destination)
    tarfile_name = os.path.basename(additional_distribution)
    if not tarfile_name.endswith(".tar.gz"):
        raise ValueError("Unrecognized additional distribution format for {}".format(additional_distribution))

    # This will overwrite the existing user flyte workflow code in the current working code dir.
    result = _subprocess.run(
        ["tar", "-xvf", os.path.join(destination, tarfile_name), "-C", destination],
        stdout=_subprocess.PIPE,
    )
    result.check_returncode()
