from pathlib import Path

cwd = Path.cwd()
home = Path.home()
print("cwd:", cwd)
print("home:", home)
data = cwd / "data"
data.mkdir(exist_ok=True)
print(data, data.exists(), data.is_dir())
