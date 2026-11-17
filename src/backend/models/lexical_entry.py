from .character import Character
from .meaning import Meaning
from .hsk_membership import HSKMembership
from .example_sentence import ExampleSentence

class LexicalEntry:
    """
        Basic lexical entry class that denotes all properites of a Chinese word/expression
            entry_id: a key that uniquely identifes each LexicalEntry
            hanzi: the hanzi representation 
            traditional: the traditional representaiton 
            pinyin: the pinyin representation
            characters: a list of all characters used in the LexicalEntry
            meanings: possible meanings for the LexicalEntry, with a list of Meaning objects
            hsk_memberships: the HSKLevel associated with the LexicalEntry; note that there may be more than one curriculum classifications, rather than a single HSK level
            examples: a list of example sentences (ExampleSentence objects)

        This class is equipped with appropriate getter methods
    """

    def __init__(self, 
                entry_id: str,
                hanzi: str, 
                traditional: str, 
                pinyin: str, 
                characters: list[Character], 
                meanings: list[Meaning], 
                hsk_memberships: list[HSKMembership], 
                examples: list[ExampleSentence]) -> None:
        
        self.entry_id = entry_id
        self.hanzi = hanzi
        self.traditional = traditional
        self.pinyin = pinyin
        self.characters = characters
        self.meanings = meanings
        self.hsk_memberships = hsk_memberships
        self.examples = examples

    def get_entry_id(self) -> str:
        return self.entry_id

    def get_hanzi(self) -> str:
        return self.hanzi

    def get_traditional(self) -> str:
        return self.traditional

    def get_pinyin(self) -> str:
        return self.pinyin

    def get_characters(self) -> list[Character]:
        return self.characters

    def get_meanings(self) -> list[Meaning]:
        return self.meanings

    def get_hsk_memberships(self) -> list[HSKMembership]:
        return self.hsk_memberships

    def get_examples(self) -> list[ExampleSentence]:
        return self.examples

    def contains_character(self, other: Character) -> bool:
        for ch in self.characters:
            if other.hanzi == ch.hanzi:
                return True

        return False

    # This one comes later
    # def to_dict(self):
    #     raise NotImplementedError("Feature not yet implemented!")