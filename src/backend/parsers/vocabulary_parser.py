import json
from src.backend.enums.hsk_version import HSKVersion
from pathlib import Path
from src.backend.enums.part_of_speech import PartOfSpeech
from src.backend.mappings.part_of_speech_map import POS_MAP
from src.backend.models.meaning import Meaning

def load_dataset(file_path: str | Path) -> list[dict] | None:
    try:
        with open(file_path, 'r', encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: {file_path} is invalid")
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format on line {e.lineno}: {e.msg}")

def parse_hsk_membership(data: list[dict]) -> dict[tuple[HSKVersion, int], list[dict]]:
    """
        Parses data according to HSK version and level
    """
    curriculum_map: dict[tuple[HSKVersion, int], list[dict]] = {}

    for item in data:
        curriculums = item.get("level", [])

        for curr in dict.fromkeys(curriculums): # Remove duplicate memberships
            ver, lvl = curr.split("-")
            hsk_ver = None

            match ver:
                case "newest":
                    hsk_ver = HSKVersion.HSK_3_2025
                case "new":
                    hsk_ver = HSKVersion.HSK_3_2021
                case "old":
                    hsk_ver = HSKVersion.HSK_2
                case _: # Data is missing, skip
                    continue

            dict_key = (hsk_ver, int(lvl))

            if dict_key not in curriculum_map:
                curriculum_map[dict_key] = [item]
            else:
                curriculum_map[dict_key].append(item)

    return curriculum_map

def parse_pos(pos_raw: list[str]) -> list[PartOfSpeech]:
    """ 
        Parse known pos abbreviations, fetch enum objects from the POS_MAP
    """
    pos_parsed = []
    seen = set()

    for raw in pos_raw:
        pos = POS_MAP.get(raw, PartOfSpeech.UNKNOWN)

        if pos not in seen:
            pos_parsed.append(pos)
            seen.add(pos)

    return pos_parsed 

def parse_meaning(meaning_raw: list[str]) -> list[Meaning]:
    parsed_meanings = []

    for meaning in meaning_raw:
        parsed_meanings.append(Meaning(meaning))

    return parsed_meanings

def parse_forms(raw_forms: list[dict]) -> list[dict]:
    parsed_forms = []
    
    for form in raw_forms:
        traditional = form["traditional"]
        transcriptions = form["transcriptions"]

        pinyin = transcriptions["pinyin"]
        numeric = transcriptions["numeric"]

        meanings = parse_meaning(form["meanings"])

        entry = {
            "traditional": traditional,
            "pinyin": pinyin,
            "numeric": numeric,
            "meanings": meanings
        }

        parsed_forms.append(entry)

    return parsed_forms

if __name__ == "__main__":
    data = load_dataset(r"data/raw/complete.json")
    print(f"Loadad data with {len(data)} entries")

    curr_data = parse_hsk_membership(data)

    lim = 0
    for k, v in curr_data.items():
        print(k)
        lim += 1

        if lim == 10:
            break