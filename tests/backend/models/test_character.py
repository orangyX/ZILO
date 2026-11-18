from src.backend.models.character import Character
from src.backend.models.meaning import Meaning
from src.backend.enums.part_of_speech import PartOfSpeech

def test_good_char() -> None:
    """
        Basic testing function; test all Character fields are populated as required
    """

    i = Character("我", ["wǒ"], [Meaning("Me", PartOfSpeech.PRONOUN)])

    assert i.get_hanzi() == "我"
    assert i.get_readings()[0] == "wǒ"
    assert i.get_meanings()[0].definition == "Me"
    assert i.get_meanings()[0].part_of_speech == PartOfSpeech.PRONOUN