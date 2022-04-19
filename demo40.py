numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

sum = 0
for v in numbers:
    sum = sum + v

print("total sum=%d" % sum)

numbers2 = [6, -5, 3, -8, 4, -2, 5, -4, 11]

for v in numbers2:
    if v < 0:
        numbers2.remove(v)

print("new numbers2=",numbers2)