class C1:
    pass
s1 = set()
s1.add(500)
s1.add(3.14)
s1.add(None)
print(s1)

s1.add(False)
print(s1)
s1.add(0)
print(s1)
s1.remove(False)
print(s1)
s1.add(False)
print(s1)

s1.add(C1())
print(s1)
s1.add(C1())
print(s1)