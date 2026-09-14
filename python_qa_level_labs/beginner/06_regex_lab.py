import re
line = "2026-09-14 TC-023 ERROR status=500"
print(re.search(r"TC-\d+", line).group())
print(re.search(r"status=(\d+)", line).group(1))
