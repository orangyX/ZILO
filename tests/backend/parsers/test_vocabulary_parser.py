from pathlib import Path
from src.backend.parsers.vocabulary_parser import (
    load_dataset,
    parse_hsk_membership,
    parse_pos,
    parse_meaning,
    parse_forms
)
import pytest
import json
from src.backend.enums.hsk_version import HSKVersion
from src.backend.enums.part_of_speech import PartOfSpeech
from src.backend.models.meaning import Meaning
from tests.fixtures.vocabulary.form_test_data.good import FORM_001, FORM_002

FIXTURES = Path(__file__).resolve().parents[2] / "fixtures" / "vocabulary" / "load_test_data"

def test_load_dataset_good() -> None:
    """
        Check that load_dataset loads a correct file
    """

    data = load_dataset(FIXTURES / "valid.json")

    assert data is not None
    assert isinstance(data, list)
    assert len(data) == 2

def test_load_dataset_adversarial() -> None:
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

def test_parse_pos_good() -> None:
    raw_pos = ["n", "ng", "nr", "v", "d", "dg"]
    parsed_pos = parse_pos(raw_pos)

    assert parsed_pos[0] == PartOfSpeech.NOUN
    assert parsed_pos[1] == PartOfSpeech.PROPER_NOUN
    assert parsed_pos[2] == PartOfSpeech.VERB
    assert parsed_pos[3] == PartOfSpeech.ADVERB

def test_parse_pos_adversarial() -> None:
    raw_pos = ["123"]
    parsed_pos = parse_pos(raw_pos)

    assert parsed_pos[0] == PartOfSpeech.UNKNOWN

def test_parse_pos_non_duplicative() -> None:
    raw_pos = ["m", "mg"]
    parsed_pos = parse_pos(raw_pos)

    assert parsed_pos == [PartOfSpeech.NUMERAL]

def test_parse_meaning_good() -> None:
    meaning_raw = ["to teach", "to play ball", "to die"]
    meanings_parsed = parse_meaning(meaning_raw)

    assert [m.get_definition() for m in meanings_parsed] == meaning_raw

def test_parse_meaning_adversarial() -> None:
    meaning_raw = []
    meanings_parsed = parse_meaning(meaning_raw)

    assert meanings_parsed == []

def test_parse_form_good() -> None:
    parsed_forms = parse_forms([FORM_001, FORM_002])

    parse_001, parse_002 = parsed_forms[0], parsed_forms[1]

    assert parse_001["traditional"] == "勸告"
    assert parse_001["pinyin"] == "quàn gào"
    assert parse_001["numeric"] == "quan4 gao4"

    assert parse_002["traditional"] == "門檻"
    assert parse_002["pinyin"] == "mén kǎn"
    assert parse_002["numeric"] == "men2 kan3"