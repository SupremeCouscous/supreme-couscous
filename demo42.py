x = range(10)
print(x)
print(type(x), list(x), len(x))

for i in range(10):
    print(i, end=" ")
print()

for i in range(10):
    print(f"do something...for step {i}")

for _ in range(10):
    print("do nothing")

x1 = range(20)
print(list(x1))
x2 = range(5, 20)
print(list(x2))
x3 = range(5, 20, 2)
print(list(x3))
x4 = range(5, 20, 3)
print(list(x4))