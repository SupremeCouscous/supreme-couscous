x1 = True
x2 = False
print(x1 and x1, x1 or x1, x2 and x2, x2 or x2)
conditions = [True, False, None, 100, 3.14, "hello world", 4 + 3j, ['hi', 'hello']]

for c in conditions:
    result = x1 and c
    print(result)
for c in conditions:
    result = x2 and c
    print(result)
for d in conditions:
    result = x2 or d
    print(result)
for d in conditions:
    result = x1 or d
    print(result)