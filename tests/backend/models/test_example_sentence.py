from src.backend.models.example_sentence import ExampleSentence

def test_example_sentence() -> None:
    eg_sentence = ExampleSentence("我是学生", "wǒ shì xuésheng", "I am a student")

    # Assertions
    assert eg_sentence.get_hanzi() == "我是学生"
    assert eg_sentence.get_pinyin() == "wǒ shì xuésheng"
    assert eg_sentence.get_english() == "I am a student"