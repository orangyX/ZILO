class ExampleSentence:
    def __init__(self, hanzi: str, pinyin: str, english: str) -> None:
        self.hanzi = hanzi
        self.pinyin = pinyin
        self.english = english

    def get_hanzi(self) -> str:
        return self.hanzi

    def get_pinyin(self) -> str:
        return self.pinyin

    def get_english(self) -> str:
        return self.english