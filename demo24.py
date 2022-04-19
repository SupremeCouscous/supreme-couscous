l1 = list('abcde12345')
l2 = ['apple', 'banana', 'citron', 'donut']
print('d' in l1, 'd' in l2, 'donut' in l2)
for f in l2:
    print("[%d]%s" % (len(f), f), end=" ")
print()
print(["[%d]%s" % (len(l), l) for l in l2])
print(l1.index('e'), l2.index('banana'))
l2.insert(2,'cookie')
print(l2)
#l2.index('bike')
print('bike' in l2, 'citron' in l2)