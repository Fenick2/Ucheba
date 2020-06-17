import re, sys

pattern = r"cat.*cat"
for line in sys.stdin:
    line = line.rstrip()
    print(*re.findall(pattern, line))
