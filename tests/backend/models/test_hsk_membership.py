from src.backend.models.hsk_membership import HSKMembership
from src.backend.enums.hsk_version import HSKVersion
import pytest

def test_valid_membership_2() -> None:
    good_lower = HSKMembership(HSKVersion.HSK_2, hsk_level=1)
    good_upper = HSKMembership(HSKVersion.HSK_2, hsk_level=6)

    # Assertions
    assert good_lower.hsk_level == 1
    assert good_lower.hsk_version == HSKVersion.HSK_2

    assert good_upper.hsk_level == 6
    assert good_upper.hsk_version == HSKVersion.HSK_2

def test_adversarial_version_2() -> None:
    # Invalid version
    with pytest.raises(ValueError):
        HSKMembership("4.0", hsk_level=1)

    # No set version
    with pytest.raises(ValueError):
            HSKMembership(None, hsk_level=1)

def test_adversarial_level_2() -> None:
    # Invalid level
    with pytest.raises(ValueError):
        HSKMembership(HSKVersion.HSK_2, hsk_level=0)

    with pytest.raises(ValueError):
        HSKMembership(HSKVersion.HSK_2, hsk_level=7)

    # No level
    with pytest.raises(ValueError):
        HSKMembership(HSKVersion.HSK_2, hsk_level=None)

def test_valid_membership_3() -> None:
    good_lower = HSKMembership(HSKVersion.HSK_3, hsk_level=1)
    good_upper = HSKMembership(HSKVersion.HSK_3, hsk_level=9)

    # Assertions
    assert good_lower.hsk_level == 1
    assert good_lower.hsk_version == HSKVersion.HSK_3

    assert good_upper.hsk_level == 9
    assert good_upper.hsk_version == HSKVersion.HSK_3

def test_adversarial_level_3() -> None:
    # Lower bound check
    with pytest.raises(ValueError):
        HSKMembership(HSKVersion.HSK_3, 0)

    # Upper bound check
    with pytest.raises(ValueError):
        HSKMembership(HSKVersion.HSK_3, 10)

    # None type check
    with pytest.raises(ValueError):
        HSKMembership(HSKVersion.HSK_3, None)

def test_adversarial_level_type() -> None:
    # Incorrect type for HSK_2 check
    with pytest.raises(ValueError):
        HSKMembership(HSKVersion.HSK_2, "1")

    # Incorrect type for HSKVersion check
    with pytest.raises(ValueError):
        HSKMembership(2.0, 1)

    # Incorrect type for HSK_3 check
    with pytest.raises(ValueError):
            HSKMembership(HSKVersion.HSK_3, "1")
    