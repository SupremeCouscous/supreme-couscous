import copy
l1 = list('abcdefg')
l2 = l1
l3 = l1[:]
l4 = copy.copy(l1)
l5 = copy.deepcopy(l1)

print(l1,l2,l3,l4,l5)

l1[0] = 'A'
print(l1, l2, l3, l4,l5 )

print(l1,l2,l3,l4,l5)