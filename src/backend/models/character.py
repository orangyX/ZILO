from .meaning import Meaning

class Character:
    def __init__(self, hanzi: str, readings: list[str], meanings: list[Meaning]) -> None:
        self.hanzi = hanzi
        self.readings = readings
        self.meanings = meanings

    def get_hanzi(self) -> str:
        return self.hanzi

    def get_readings(self) -> list[str]:
        return self.readings

    def get_meanings(self) -> list[Meaning]:
        return self.meanings

    # To be implemented
    # def stroke_count(self):
        # eturn self.stroke_count

    # def radical(self):
        # return self.radical

    # def components(self):
        # return self.components