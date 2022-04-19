from copy import copy, deepcopy

l1 = [['A','K'], ['Q','J']]
l2 = l1
print(l1,l2)

l3 = copy(l1)
l4 = deepcopy(l1)
print(l3,l4)

l1.append('JOKER')
print(l1,l2,l3,l4)

l1[0][0] = 'Z'
print(l1, l2, l3, l4)