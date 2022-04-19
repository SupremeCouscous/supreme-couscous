l2 = [('s', 15), ('m', 20), ('l', 15), ('xl', 10), ('m', 20), ('l', 15), ('xl', 10), ('xl', 10), ('m', 20)]

sales = {}
for size, quantity in l2:
    sales.setdefault(size,0)
    sales[size] += quantity

print(l2)
print(sales)
