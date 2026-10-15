import json
from pathlib import Path

def load_model_data(file_path : str = "models.json") -> list[dict]:

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError("File does not exist.")

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data

if __name__ == "__main__":
    load_model_data()