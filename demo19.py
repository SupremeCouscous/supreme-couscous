x1 = [1, 2, 3, 4, 5]
x2 = x1
x3 = [1, 2, 3, 4, 5]
print(x1, x2, x3)
print(x1 == x2, x1 == x3)
print(x1 is x2, x1 is x3)
print(f"x1 id={hex(id(x1))}")
print(f"x2 id={hex(id(x2))}")
print(f"x3 id={hex(id(x3))}")
x1[0] += 100
print(x1, x2, x3)