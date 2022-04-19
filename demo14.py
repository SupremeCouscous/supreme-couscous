a = 17
b = 3
print(a + b, a - b, a / b)
print(a/b, a//b, a%b)
print(a **b, b**a)
c = 4.1
print(round(c))
cs = [4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9]

for i in range(10):
    for c in cs:
        print(round(c=i, end = " "))
    print()