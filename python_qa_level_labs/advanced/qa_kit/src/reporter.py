import json
from pathlib import Path

DEFAULT_PATH = "artifacts/results.json"

def save_report(results, path=DEFAULT_PATH):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
