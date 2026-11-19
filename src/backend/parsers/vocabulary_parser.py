import json
from src.backend.enums.hsk_version import HSKVersion
from pathlib import Path
from src.backend.enums.part_of_speech import PartOfSpeech
from src.backend.mappings.part_of_speech_map import POS_MAP

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

def parse_pos(curr_data: dict[tuple[HSKVersion, int], list[dict]]) -> None: # For now
    raise NotImplementedError("Not yet implemented")

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