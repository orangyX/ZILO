from src.backend.enums.part_of_speech import PartOfSpeech

POS_MAP: dict[str, PartOfSpeech] = {
    "n": PartOfSpeech.NOUN,
    "ng": PartOfSpeech.NOUN,

    "nr": PartOfSpeech.PROPER_NOUN,
    "ns": PartOfSpeech.PROPER_NOUN,
    "nt": PartOfSpeech.PROPER_NOUN,
    "nz": PartOfSpeech.PROPER_NOUN,

    "v": PartOfSpeech.VERB,
    "vg": PartOfSpeech.VERB,
    "vd": PartOfSpeech.VERB,
    "vn": PartOfSpeech.VERB,

    "a": PartOfSpeech.ADJECTIVE,
    "ad": PartOfSpeech.ADJECTIVE,
    "ag": PartOfSpeech.ADJECTIVE,
    "an": PartOfSpeech.ADJECTIVE,
    "b": PartOfSpeech.ADJECTIVE,

    "d": PartOfSpeech.ADVERB,
    "dg": PartOfSpeech.ADVERB,

    "r": PartOfSpeech.PRONOUN,
    "rg": PartOfSpeech.PRONOUN,

    "c": PartOfSpeech.CONJUNCTION,
    "p": PartOfSpeech.PREPOSITION,
    "e": PartOfSpeech.INTERJECTION,

    "m": PartOfSpeech.NUMERAL,
    "mg": PartOfSpeech.NUMERAL,

    "q": PartOfSpeech.CLASSIFIER,
    "y": PartOfSpeech.PARTICLE,
    "u": PartOfSpeech.AUXILIARY,
    "i": PartOfSpeech.IDIOM,
    "l": PartOfSpeech.EXPRESSION,

    "t": PartOfSpeech.TIME_WORD,
    "tg": PartOfSpeech.TIME_WORD,

    "f": PartOfSpeech.LOCATION_WORD,
    "s": PartOfSpeech.LOCATION_WORD,

    "x": PartOfSpeech.UNKNOWN, 
    "Mg": PartOfSpeech.UNKNOWN,
    "Rg": PartOfSpeech.UNKNOWN,
    "cc": PartOfSpeech.UNKNOWN,
    "g": PartOfSpeech.UNKNOWN,
    "h": PartOfSpeech.UNKNOWN,
    "k": PartOfSpeech.UNKNOWN,
    "mq": PartOfSpeech.UNKNOWN,
    "o": PartOfSpeech.UNKNOWN,
    "qt": PartOfSpeech.UNKNOWN,
    "qv": PartOfSpeech.UNKNOWN,
    "z": PartOfSpeech.UNKNOWN, # Aparrently Python allows this, and it makes adding more entries easier?
}