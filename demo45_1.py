import sys

text = ""
print("randomly input something...")
# while True:
#     c = sys.stdin.read(1)
#     text = text + c
#     if c == '\n':
#         break
while (c := sys.stdin.read(1)) != '\n':
    text = text + c

#print("input %s, len=%d" % (text[:-1], len(text[:-1])))
print("input %s, len=%d" % (text, len(text)))