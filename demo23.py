
list1 = list('abcde')
list2 = list('abcde')
list3 = list('abcde')
print(list1)
print(list1 + list1)
print(list1 * 2)
list1.append('f')
print(list1)
list2.extend('f')
print(list2)
list3 += ['f']
print(list3)
list1.append(['g','h'])
print(list1)
list2.extend(['g','h'])
print(list2)
list3 += ['g','h']
print(list3)