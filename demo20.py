x = 5
print("x=%d, id=%s" % (x, hex(id(x))))
x = 6
print("x=%d, id=%s" % (x, hex(id(x))))
y = [5]
print("y[0]=%d, y id=%s" % (y[0], hex(id(y))))
y[0] = 6
print("y[0]=%d, y id=%s" % (y[0], hex(id(y))))

