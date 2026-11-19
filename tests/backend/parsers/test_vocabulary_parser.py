from pathlib import Path
from src.backend.parsers.vocabulary_parser import (
    load_dataset,
    parse_hsk_membership
)
import pytest
import json
from src.backend.enums.hsk_version import HSKVersion

FIXTURES = Path("tests/fixtures/vocabulary")

def test_load_dataset_good() -> None:
    """
        Check that load_dataset loads a correct file
    """

    data = load_dataset(FIXTURES / "valid.json")

    assert data is not None
    assert isinstance(data, list)
    assert len(data) == 2

def test_load_dataset_bad() -> None:
    """
        Check that load_dataset returns None on a malformed file
    """

    data = load_dataset(FIXTURES / "invalid.json")

    assert data is None

def test_load_dataset_empty() -> None:
    """
        Check that load_dataset returns [] on an empty json file
    """

    data = load_dataset(FIXTURES / "empty.json")

    assert len(data) == 0
    assert isinstance(data, list)

def test_parse_hsk_membership_good() -> None:
    """
        Check that parse_hsk_membership:
            - Has correct HSKVersion objects
            - HSK level is an int
            - Parsed keys are correct
            - Hanzi is correct
    """

    data = parse_hsk_membership(load_dataset(FIXTURES / "multiple_curriculums.json"))
    hsk_vers = [HSKVersion.HSK_2, HSKVersion.HSK_3_2021, HSKVersion.HSK_3_2025]

    for k, _ in data.items():
        ver, lvl = k

        assert ver in hsk_vers
        assert isinstance(lvl, int)

    assert (HSKVersion.HSK_2, 1) in data
    assert (HSKVersion.HSK_3_2021, 1) in data
    assert (HSKVersion.HSK_3_2025, 1) in data
    assert data[(HSKVersion.HSK_2, 1)][0]["simplified"] == "我"
    assert data[(HSKVersion.HSK_2, 1)][1]["simplified"] == "你"