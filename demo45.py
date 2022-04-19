import sys
text = ""
print("randomly input something...")
while True:
    c = sys.stdin.read(1)
    text = text + c
    if c == '\n':
        break
print("input %s, len ")