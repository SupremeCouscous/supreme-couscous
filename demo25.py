import random

l1 = [r + 1 for r in range(10)]
print(l1)
random.shuffle(l1)
print(l1)
l1.sort()
print(l1)
l2 = [1, 3, 5, 'a', 'b', 'c']
# l2.sort()
l3 = ['1', '3', '5', 'a', 'b', 'c']
random.shuffle(l3)
print(l3)
l3.sort()
l4 = list('j30921j30912FJIDSJFS')
l4.sort()
print(l4)