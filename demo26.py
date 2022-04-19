l1 = list('acebd')
l1.sort()
print(l1)
l1.sort(reverse=True)
print(l1)
s2 = 'abcdefg1234567'
l2 = list(s2)
print(l2)
print(s2)
for l in l2:
    print(f"[{l}]", end=" ")
print()
for s in s2:
    print(f"[{s}]", end=" ")
print()
print('c' in l2, 'c' in s2)
l2[0] = '*'
print(l2)
# s2[0]='*'
# print(s2)
s2 = '*' + s2[1:]
print(s2)