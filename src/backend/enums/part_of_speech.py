from enum import Enum


class PartOfSpeech(Enum):
    NOUN = "noun"
    PROPER_NOUN = "proper noun"
    VERB = "verb"
    ADJECTIVE = "adjective"
    ADVERB = "adverb"
    PRONOUN = "pronoun"
    CONJUNCTION = "conjunction"
    PREPOSITION = "preposition"
    INTERJECTION = "interjection"
    NUMERAL = "numeral"
    CLASSIFIER = "classifier"
    PARTICLE = "particle"
    AUXILIARY = "auxiliary"
    IDIOM = "idiom"
    EXPRESSION = "expression"
    TIME_WORD = "time word"
    LOCATION_WORD = "location word"
    UNKNOWN = "unknown"