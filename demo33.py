l1 = list('smmlsmmlsmmlmlsmmlmlsmmlmlsmmlmlsmmlmlsmml')
print(l1)
# sales = {}
sales = {'s': 0, 'm': 0, 'l': 0}
for g in l1:
    sales[g] = sales[g] + 1
print(sales)