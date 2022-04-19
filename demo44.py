n = 200
summation = 0
counter = 1

while counter <= n:
    summation += counter
    counter += 1
    pass
else:
    print ('calculation terminated')

print("sum from 1 to %d is %d" % (n,summation))