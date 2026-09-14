import json
from pathlib import Path

def load_cases(path="data/cases.json"):
    return json.loads(Path(path).read_text(encoding="utf-8"))
