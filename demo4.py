import sys
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()

fib(1000)

def fib2(n):
    result = []
    a, b = 0,1
    while a < n:
        a, b = b, a + b
        result.append(a)
    return result
fib(1000)
fib(100)
print(fib2(100))
print(fib2(1000))
if __name__ == '__main__':
    fib(int(sys.argv[1]))
