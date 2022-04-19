l1 = list('123456789') * 2
print(l1)
print(l1[3:6])  # 4th, 5th, 6th,
print(l1[:6], l1[6:])
print(l1[:-6], l1[-6:])
print("reverse", l1[6:3])

print(l1[-6:-3], l1[-3:-6])
print(l1[:])
print(l1[::2])