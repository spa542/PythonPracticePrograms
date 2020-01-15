# Fibonacci Exercise

def fib(number):
    if number == 0:
        return 0
    if number == 1:
        return 1
    return fib(number-1) + fib(number-2)

print(fib(20))

def fibo(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        temp = a
        a = b
        b = temp + b

# Highly inefficient
for x in fibo(100):
    print(x)
