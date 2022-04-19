l1 = list('smmlsmmlsmmlmlsmmlmlsmmlmlsmgmlmlsmmglmlsmgmlf')
print(l1)
sales = {}
# sales = {'s': 0, 'm': 0, 'l': 0}
for l in l1:
    sales.setdefault(l, 0)
    sales[l] = sales[l] + 1
print(sales)