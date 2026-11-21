from ..enums.part_of_speech import PartOfSpeech # .. because it is a sibling directory

class Meaning:
    """
        Minimal Meaning class; a character/lexical entry stores a list of Meaning objects
    """

    def __init__(self, definition: str, part_of_speech=PartOfSpeech|None) -> None:
        self.definition = definition
        self.part_of_speech = part_of_speech

    def get_definition(self) -> str:
        return self.definition

    def get_part_of_speech(self) -> PartOfSpeech:
        return self.part_of_speech