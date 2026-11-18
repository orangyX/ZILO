from src.backend.models.meaning import Meaning
from src.backend.enums.part_of_speech import PartOfSpeech

def test_meaning() -> None:
    i = Meaning("I", PartOfSpeech.PRONOUN)

    # Assertions
    assert i.get_definition() == "I"
    assert i.get_part_of_speech() == PartOfSpeech.PRONOUN