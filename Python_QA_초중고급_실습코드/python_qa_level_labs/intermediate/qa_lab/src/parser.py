import re
PATTERN = re.compile(r"(?P<tc>TC-\d+)\s+(?P<level>INFO|WARN|ERROR)\s+status=(?P<status>\d+)")
def parse_line(line):
    m = PATTERN.search(line)
    return m.groupdict() if m else None
