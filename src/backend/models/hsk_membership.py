from ..enums.hsk_version import HSKVersion

class HSKMembership:
    def __init__(self, hsk_version: HSKVersion, hsk_level: int) -> None:
        self.hsk_version = hsk_version

        if not self._validate_level(hsk_level):
            raise ValueError(f"{hsk_level} is invalid for {self.hsk_version}")

        self.hsk_level = hsk_level

    def get_hsk_version(self) -> HSKVersion:
        return self.hsk_version

    def get_hsk_level(self) -> int:
        return self.hsk_level

    def _validate_level(self, hsk_level: int) -> bool:
        if type(hsk_level) is not int: # not isinstance(hsk_level, int) yields true due to double negation
            return False
        elif self.hsk_version == HSKVersion.HSK_2:
            return 1 <= hsk_level <= 6
        elif self.hsk_version in (HSKVersion.HSK_3_2021, HSKVersion.HSK_3_2025):
            return 1 <= hsk_level <= 9

        return False # Something else went wrong; perhaps the version is incorrect