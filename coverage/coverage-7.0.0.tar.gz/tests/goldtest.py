# Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
# For details: https://github.com/nedbat/coveragepy/blob/master/NOTICE.txt

"""A test base class for tests based on gold file comparison."""

import difflib
import filecmp
import fnmatch
import os
import os.path
import re
import xml.etree.ElementTree

from tests.coveragetest import TESTS_DIR
from tests.helpers import os_sep


def gold_path(path):
    """Get a path to a gold file for comparison."""
    return os.path.join(TESTS_DIR, "gold", path)


def compare(
        expected_dir, actual_dir, file_pattern=None,
        actual_extra=False, scrubs=None,
        ):
    """Compare files matching `file_pattern` in `expected_dir` and `actual_dir`.

    `actual_extra` true means `actual_dir` can have extra files in it
    without triggering an assertion.

    `scrubs` is a list of pairs: regexes to find and replace to scrub the
    files of unimportant differences.

    If a comparison fails, a message will be written to stdout, the original
    unscrubbed output of the test will be written to an "/actual/" directory
    alongside the "/gold/" directory, and an assertion will be raised.

    """
    __tracebackhide__ = True    # pytest, please don't show me this function.
    assert os_sep("/gold/") in expected_dir

    dc = filecmp.dircmp(expected_dir, actual_dir)
    diff_files = fnmatch_list(dc.diff_files, file_pattern)
    expected_only = fnmatch_list(dc.left_only, file_pattern)
    actual_only = fnmatch_list(dc.right_only, file_pattern)

    def save_mismatch(f):
        """Save a mismatched result to tests/actual."""
        save_path = expected_dir.replace(os_sep("/gold/"), os_sep("/actual/"))
        os.makedirs(save_path, exist_ok=True)
        with open(os.path.join(save_path, f), "w") as savef:
            with open(os.path.join(actual_dir, f)) as readf:
                savef.write(readf.read())

    # filecmp only compares in binary mode, but we want text mode.  So
    # look through the list of different files, and compare them
    # ourselves.
    text_diff = []
    for f in diff_files:
        expected_file = os.path.join(expected_dir, f)
        with open(expected_file) as fobj:
            expected = fobj.read()
        if expected_file.endswith(".xml"):
            expected = canonicalize_xml(expected)

        actual_file = os.path.join(actual_dir, f)
        with open(actual_file) as fobj:
            actual = fobj.read()
        if actual_file.endswith(".xml"):
            actual = canonicalize_xml(actual)

        if scrubs:
            expected = scrub(expected, scrubs)
            actual = scrub(actual, scrubs)
        if expected != actual:
            text_diff.append(f'{expected_file} != {actual_file}')
            expected = expected.splitlines()
            actual = actual.splitlines()
            print(f":::: diff '{expected_file}' and '{actual_file}'")
            print("\n".join(difflib.Differ().compare(expected, actual)))
            print(f":::: end diff '{expected_file}' and '{actual_file}'")
            save_mismatch(f)

    if not actual_extra:
        for f in actual_only:
            save_mismatch(f)

    assert not text_diff, "Files differ: " + "\n".join(text_diff)

    assert not expected_only, f"Files in {expected_dir} only: {expected_only}"
    if not actual_extra:
        assert not actual_only, f"Files in {actual_dir} only: {actual_only}"


def contains(filename, *strlist):
    """Check that the file contains all of a list of strings.

    An assert will be raised if one of the arguments in `strlist` is
    missing in `filename`.

    """
    __tracebackhide__ = True    # pytest, please don't show me this function.
    with open(filename) as fobj:
        text = fobj.read()
    for s in strlist:
        assert s in text, f"Missing content in {filename}: {s!r}"


def contains_rx(filename, *rxlist):
    """Check that the file has lines that re.search all of the regexes.

    An assert will be raised if one of the regexes in `rxlist` doesn't match
    any lines in `filename`.

    """
    __tracebackhide__ = True    # pytest, please don't show me this function.
    with open(filename) as fobj:
        lines = fobj.readlines()
    for rx in rxlist:
        assert any(re.search(rx, line) for line in lines), (
            f"Missing regex in {filename}: r{rx!r}"
        )


def contains_any(filename, *strlist):
    """Check that the file contains at least one of a list of strings.

    An assert will be raised if none of the arguments in `strlist` is in
    `filename`.

    """
    __tracebackhide__ = True    # pytest, please don't show me this function.
    with open(filename) as fobj:
        text = fobj.read()
    for s in strlist:
        if s in text:
            return

    assert False, f"Missing content in {filename}: {strlist[0]!r} [1 of {len(strlist)}]"


def doesnt_contain(filename, *strlist):
    """Check that the file contains none of a list of strings.

    An assert will be raised if any of the strings in `strlist` appears in
    `filename`.

    """
    __tracebackhide__ = True    # pytest, please don't show me this function.
    with open(filename) as fobj:
        text = fobj.read()
    for s in strlist:
        assert s not in text, f"Forbidden content in {filename}: {s!r}"


# Helpers

def canonicalize_xml(xtext):
    """Canonicalize some XML text."""
    root = xml.etree.ElementTree.fromstring(xtext)
    for node in root.iter():
        node.attrib = dict(sorted(node.items()))
    xtext = xml.etree.ElementTree.tostring(root)
    return xtext.decode("utf-8")


def fnmatch_list(files, file_pattern):
    """Filter the list of `files` to only those that match `file_pattern`.
    If `file_pattern` is None, then return the entire list of files.
    Returns a list of the filtered files.
    """
    if file_pattern:
        files = [f for f in files if fnmatch.fnmatch(f, file_pattern)]
    return files


def scrub(strdata, scrubs):
    """Scrub uninteresting data from the payload in `strdata`.
    `scrubs` is a list of (find, replace) pairs of regexes that are used on
    `strdata`.  A string is returned.
    """
    for rx_find, rx_replace in scrubs:
        strdata = re.sub(rx_find, rx_replace, strdata)
    return strdata
