print("Hello, World!")

def fib(n):
    a, b = 0, 1
    for i in range(n):
        if i > 0:
            a, b = b, a + b
    return a

print(fib(10))
