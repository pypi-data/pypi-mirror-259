"""
Test suite for the module [ews_env.version](site:api/ews_env/version).
"""

import re
from datetime import datetime

from packaging.version import (
    Version,
    parse as parse_version,  # pyright: ignore [reportMissingImports]
)

import ews_nox


def test_version_info():
    """Test the version_info"""
    s = ews_nox.version_info()
    assert re.match(" *ews_nox version: ", s)
    assert s.count("\n") == 4


def test_standard_version():
    """Test the standard version"""
    v = parse_version(ews_nox.VERSION)
    assert str(v) == ews_nox.VERSION


def test_version_attribute_is_present():
    """Test that __version__ is present"""
    assert hasattr(ews_nox, "__version__")


def test_version_attribute_is_a_string():
    """Test that __version__ is a string"""
    assert isinstance(ews_nox.__version__, str)


def test_version_is_datever():
    """Test that __version__ is a string"""
    v = Version(ews_nox.VERSION)
    assert len(v.release) in [1, 2], v
    main = v.release[0]
    patch = 0 if len(v.release) == 1 else v.release[1]
    assert re.match(r"\d\d\d\d\d\d", str(main)), v.release
    main = str(main)
    assert re.match(r"\d+", str(patch)), v.release
    assert datetime.strptime(main, "%Y%m%d")  # noqa: DTZ007
