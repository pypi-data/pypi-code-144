"""QIIME2 private functions for HiTaC."""
import json
import os
import tarfile

import joblib
import qiime2.plugin
import qiime2.plugin.model as model
import sklearn
from hiclass import LocalClassifierPerParentNode

from .filter import Filter
from .plugin_setup import plugin

# Semantic Types
HierarchicalTaxonomicClassifier = qiime2.plugin.SemanticType(
    "HierarchicalTaxonomicClassifier"
)


# Formats
class PickleFormat(model.BinaryFileFormat):
    """Class for PickleFormat."""

    def sniff(self):
        """
        Check if file is TAR.

        Returns
        -------
        _ : bool
            True if file is TAR compressed, otherwise false.
        """
        return tarfile.is_tarfile(str(self))


# https://github.com/qiime2/q2-types/issues/49
class JSONFormat(model.TextFileFormat):
    """Class for JSONFormat."""

    def sniff(self):
        """
        Check JSON file is valid.

        Returns
        -------
        _ : bool
            True if file is JSON file is valid, otherwise false.
        """
        with self.open() as fh:
            try:
                json.load(fh)
                return True
            except json.JSONDecodeError:
                pass
        return False


class HierarchicalTaxonomicClassifierDirFmt(model.DirectoryFormat):
    """Class for HierarchicalTaxonomicClassifierDirFmt."""

    preprocess_params = model.File("preprocess_params.json", format=JSONFormat)
    sklearn_pipeline = model.File("sklearn_pipeline.tar", format=PickleFormat)


class HierarchicalTaxonomicClassiferTemporaryPickleDirFmt(model.DirectoryFormat):
    """Class for HierarchicalTaxonomicClassiferTemporaryPickleDirFmt."""

    version_info = model.File("sklearn_version.json", format=JSONFormat)
    sklearn_pipeline = model.File("sklearn_pipeline.tar", format=PickleFormat)


# Transformers
@plugin.register_transformer
def _1(
    dirfmt: HierarchicalTaxonomicClassiferTemporaryPickleDirFmt,
) -> LocalClassifierPerParentNode:
    sklearn_version = dirfmt.version_info.view(dict)["sklearn-version"]
    if sklearn_version != sklearn.__version__:
        raise ValueError(
            "The scikit-learn version (%s) used to generate this"
            " artifact does not match the current version"
            " of scikit-learn installed (%s). Please retrain your"
            " classifier for your current deployment to prevent"
            " data-corruption errors." % (sklearn_version, sklearn.__version__)
        )

    sklearn_pipeline = dirfmt.sklearn_pipeline.view(PickleFormat)

    with tarfile.open(str(sklearn_pipeline)) as tar:
        tmpdir = model.DirectoryFormat()
        dirname = str(tmpdir)
        tar.extractall(dirname)
        pipeline = joblib.load(os.path.join(dirname, "sklearn_pipeline.pkl"))
        for fn in tar.getnames():
            os.unlink(os.path.join(dirname, fn))

    return pipeline


@plugin.register_transformer
def _2(
    data: LocalClassifierPerParentNode,
) -> HierarchicalTaxonomicClassiferTemporaryPickleDirFmt:
    sklearn_pipeline = PickleFormat()
    with tarfile.open(str(sklearn_pipeline), "w") as tar:
        tmpdir = model.DirectoryFormat()
        pf = os.path.join(str(tmpdir), "sklearn_pipeline.pkl")
        for fn in joblib.dump(data, pf):
            tar.add(fn, os.path.basename(fn))
            os.unlink(fn)

    dirfmt = HierarchicalTaxonomicClassiferTemporaryPickleDirFmt()
    dirfmt.version_info.write_data({"sklearn-version": sklearn.__version__}, dict)
    dirfmt.sklearn_pipeline.write_data(sklearn_pipeline, PickleFormat)

    return dirfmt


@plugin.register_transformer
def _3(dirfmt: HierarchicalTaxonomicClassifierDirFmt) -> LocalClassifierPerParentNode:
    raise ValueError(
        "The scikit-learn version could not be determined for"
        " this artifact, please retrain your classifier for your"
        " current deployment to prevent data-corruption errors."
    )


@plugin.register_transformer
def _4(fmt: JSONFormat) -> dict:
    with fmt.open() as fh:
        return json.load(fh)


@plugin.register_transformer
def _5(data: dict) -> JSONFormat:
    result = JSONFormat()
    with result.open() as fh:
        json.dump(data, fh)
    return result


# Transformers
@plugin.register_transformer
def _6(
    dirfmt: HierarchicalTaxonomicClassiferTemporaryPickleDirFmt,
) -> Filter:
    sklearn_version = dirfmt.version_info.view(dict)["sklearn-version"]
    if sklearn_version != sklearn.__version__:
        raise ValueError(
            "The scikit-learn version (%s) used to generate this"
            " artifact does not match the current version"
            " of scikit-learn installed (%s). Please retrain your"
            " classifier for your current deployment to prevent"
            " data-corruption errors." % (sklearn_version, sklearn.__version__)
        )

    sklearn_pipeline = dirfmt.sklearn_pipeline.view(PickleFormat)

    with tarfile.open(str(sklearn_pipeline)) as tar:
        tmpdir = model.DirectoryFormat()
        dirname = str(tmpdir)
        tar.extractall(dirname)
        pipeline = joblib.load(os.path.join(dirname, "sklearn_pipeline.pkl"))
        for fn in tar.getnames():
            os.unlink(os.path.join(dirname, fn))

    return pipeline


@plugin.register_transformer
def _7(
    data: Filter,
) -> HierarchicalTaxonomicClassiferTemporaryPickleDirFmt:
    sklearn_pipeline = PickleFormat()
    with tarfile.open(str(sklearn_pipeline), "w") as tar:
        tmpdir = model.DirectoryFormat()
        pf = os.path.join(str(tmpdir), "sklearn_pipeline.pkl")
        for fn in joblib.dump(data, pf):
            tar.add(fn, os.path.basename(fn))
            os.unlink(fn)

    dirfmt = HierarchicalTaxonomicClassiferTemporaryPickleDirFmt()
    dirfmt.version_info.write_data({"sklearn-version": sklearn.__version__}, dict)
    dirfmt.sklearn_pipeline.write_data(sklearn_pipeline, PickleFormat)

    return dirfmt


@plugin.register_transformer
def _8(dirfmt: HierarchicalTaxonomicClassifierDirFmt) -> Filter:
    raise ValueError(
        "The scikit-learn version could not be determined for"
        " this artifact, please retrain your classifier for your"
        " current deployment to prevent data-corruption errors."
    )


# Registrations
plugin.register_semantic_types(HierarchicalTaxonomicClassifier)
plugin.register_formats(
    HierarchicalTaxonomicClassifierDirFmt,
    HierarchicalTaxonomicClassiferTemporaryPickleDirFmt,
)
plugin.register_semantic_type_to_format(
    HierarchicalTaxonomicClassifier,
    artifact_format=HierarchicalTaxonomicClassiferTemporaryPickleDirFmt,
)
