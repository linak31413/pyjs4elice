import json
from pathlib import Path

DEFAULT_PATH = "data/cases.json"

def load_cases(path=DEFAULT_PATH):
    return json.loads(Path(path).read_text(encoding="utf-8"))
