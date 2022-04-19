import demo4
import demo4 as d

demo4.fib(100)
print(demo4.fib2(200))
d.fib(300)
print(d.fib2(200))

from demo4 import fib
fib(400)
from demo4 import fib as f
f(500)