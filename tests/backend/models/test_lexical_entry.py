from src.backend.models.lexical_entry import LexicalEntry
from src.backend.models.character import Character
from src.backend.models.meaning import Meaning
from src.backend.models.hsk_membership import HSKMembership
from src.backend.models.example_sentence import ExampleSentence
from src.backend.enums.part_of_speech import PartOfSpeech
from src.backend.enums.hsk_version import HSKVersion

def test_good_lexical_entry() -> None:
    """
        Standard test case, testing all attributes of a proper, non-adversarial input
    """

    good_lexical = LexicalEntry(
                                entry_id="test_001", 
                                hanzi="我", 
                                traditional="我", 
                                pinyin="wǒ",
                                characters=[Character("我", readings=["wǒ"], meanings=[Meaning(definition="I", part_of_speech=PartOfSpeech.PRONOUN)])],
                                hsk_memberships=[HSKMembership(hsk_version=HSKVersion.HSK_2, hsk_level=1), HSKMembership(HSKVersion.HSK_3, 1)],
                                meanings=[Meaning("I", PartOfSpeech.PRONOUN), Meaning("Myself", PartOfSpeech.PRONOUN)],
                                examples=[ExampleSentence(hanzi="我是学生", pinyin="wǒ shì xuéshēng", english="I am a student"), ExampleSentence(hanzi="我星期二没有课", pinyin="wǒ xīngqī'èr méiyǒu kè", english="I don't have class on Tuesday")]
                                )

    # Assertions
    assert good_lexical.get_entry_id() == "test_001"
    assert good_lexical.get_hanzi() == "我"
    assert good_lexical.get_traditional() == "我"
    assert good_lexical.get_pinyin() == "wǒ"

    character = good_lexical.get_characters()[0]

    assert character.get_hanzi() == "我"
    assert character.get_readings()[0] == "wǒ"
    assert character.get_meanings()[0].get_definition() == "I"
    assert character.get_meanings()[0].get_part_of_speech() == PartOfSpeech.PRONOUN

    hsk_members = good_lexical.get_hsk_memberships()

    assert hsk_members[0].get_hsk_version() == HSKVersion.HSK_2
    assert hsk_members[0].get_hsk_level() == 1

    assert hsk_members[1].get_hsk_version() == HSKVersion.HSK_3
    assert hsk_members[1].get_hsk_level() == 1

    means = good_lexical.get_meanings()

    assert means[0].get_definition() == "I" 
    assert means[0].get_part_of_speech() == PartOfSpeech.PRONOUN
    assert means[1].get_definition() == "Myself" 
    assert means[1].get_part_of_speech() == PartOfSpeech.PRONOUN

    eg_sentences = good_lexical.get_examples()

    assert eg_sentences[0].get_hanzi() == "我是学生" 
    assert eg_sentences[0].get_pinyin() == "wǒ shì xuéshēng" 
    assert eg_sentences[0].get_english() == "I am a student"
    assert eg_sentences[1].get_hanzi() == "我星期二没有课" 
    assert eg_sentences[1].get_pinyin() == "wǒ xīngqī'èr méiyǒu kè" and eg_sentences[1].get_english() == "I don't have class on Tuesday"

def test_lexical_composition() -> None:
    """
        Check all contains_character() fields work as required
    """

    # A lot of None attributes since I do not care about them in this test case
    lexical_case = LexicalEntry(
        entry_id="test_002",
        hanzi="学生",
        traditional="學生",
        pinyin="xuéshēng",
        characters=[Character(hanzi="学", readings=["xué"], meanings=[Meaning(definition="to study", part_of_speech=PartOfSpeech.VERB)]), Character(hanzi="生", readings=["shēng"], meanings=[Meaning("to grow", PartOfSpeech.VERB), Meaning("to give birth", PartOfSpeech.VERB), Meaning("to be born", PartOfSpeech.VERB)])], # There are more cases, but I will not encode them here
        hsk_memberships=[],
        meanings = [],
        examples = []
    )

    assert lexical_case.contains_character(Character(hanzi="生", readings=None, meanings=None))
    assert lexical_case.contains_character(Character(hanzi="学", readings=None, meanings=None))
    assert not lexical_case.contains_character(Character(hanzi="我", readings=None, meanings=None))

def test_lexical_lengths() -> None:
    """
        Check that the attributes of LexicalEntry are populated with the correct number of arguments
    """

    lexical_case = LexicalEntry(
        entry_id="test_003",
        hanzi="早饭",
        traditional="早飯",
        pinyin="zǎo fàn",
        characters=[Character(hanzi="早", readings=None, meanings=None), Character(hanzi="饭", readings=None, meanings=None)],
        hsk_memberships=[HSKMembership(hsk_version=HSKVersion.HSK_3, hsk_level=1)],
        meanings = [Meaning(definition="breakfast", part_of_speech=PartOfSpeech.NOUN)],
        examples=[ExampleSentence(hanzi="明天早上我们一起去咖啡馆吃早饭吧", pinyin="míngtiān zǎoshang wǒmen yìqǐ qù kāfēiguǎn chī zǎofàn ba", english="Let's eat breakfast at the cafe tomorrow morning")]
    )

    assert len(lexical_case.get_characters()) == 2
    assert len(lexical_case.get_hsk_memberships()) == 1
    assert len(lexical_case.get_meanings()) == 1
    assert len(lexical_case.get_examples()) == 1

def test_empty_character_collection() -> None:
    empty_case = LexicalEntry(entry_id="test_004", hanzi="学习", traditional="學習", pinyin="xuéxí", characters=[], meanings=[], hsk_memberships=[], examples=[])

    assert not empty_case.contains_character(Character(hanzi="学", readings=[], meanings=[]))