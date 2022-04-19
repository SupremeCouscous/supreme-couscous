d1 = {'name': 'poop', 'duration': 35}
d2 = {'duration': 35, 'name': 'poop'}
d3 = dict(name="poop", duration=35)
d4 = dict([('name', 'poop'), ('duration', 35)])
print(d1, d2, d3, d4)
print(d1 == d2, d1 == d3, d1 == d4)

for d in d1:
    print(f"key={d}, value={d1[d]}")
for k in d1.keys():
    print(f"key={k}, value={d1[k]}")
for v in d1.values():
    print(f"value={v}")
for i in d1.items():
    print(type(i), i)
    print(f"key={i[0]}, value={i[1]}")
for k, v in d1.items():
    print(f"key={k},value={v}")