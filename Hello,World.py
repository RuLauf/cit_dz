print("Hello, World!")

def fib(n):
    fib_list = [0, 1]
    for i in range(2, n):
        fib_list.append(fib_list[i-1] + fib_list[i-2])
    for num in fib_list:
        print(num)

fib(10)