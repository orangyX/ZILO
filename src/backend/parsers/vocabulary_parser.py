import json

def load_dataset(file_path: str) -> list[dict] | None:
    try:
        with open(file_path, 'r', encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: {file_path} is invalid")
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format on line {e.lineno}: {e.msg}")

if __name__ == "__main__":
    data = load_dataset(r"data/raw/complete.json")
    print(len(data))
    print(type(data))
    print(type(data[0]))
    print(data[0].keys())

    print(json.dumps(data[0], indent=4, ensure_ascii=False))