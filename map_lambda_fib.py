cube = lambda x: x**3

def my_fibo(n):
    return n+1

def fibonacci(n):
    fibo = map(my_fibo, [n])
    print(fibo)
