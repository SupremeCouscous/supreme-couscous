a = ()
b = ('hello')
c = ('hello',)
d = ['hello']
print(type(a), type(b), type(c), type(d))
y1 = ['hello']
y2 = ('hello',)
y1[0] = 'HELLO'
print(y1)
# y2[0] = 'HELLO'
t1 = 5
t2 = 3
print(t1, t2)
temp = t1
t1 = t2
t2 = temp
print(t1, t2)
t1, t2 = t2, t1
print(t1, t2)
t3 = 5
t4 = 'hello'
print(t3, t4)
t3, t4 = t4, t3
print(t3, t4)
xt1, xt2, xt3, xt4, xt5 = ('A', 'K', 'Q', 'J', 10)
print(xt1, xt2, xt3, xt4, xt5)
xt5, xt2, xt1, xt3, xt4 = xt1, xt2, xt3, xt4, xt5
print(xt1, xt2, xt3, xt4, xt5)