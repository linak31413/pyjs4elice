from pathlib import Path
base = Path("data")
for p in base.rglob("*.log"):
    print(p.name)
