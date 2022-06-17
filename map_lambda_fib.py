cube = lambda x: x**3

def fibonacci(n):
    fibo = [0, 1]
    if n == 1 or n == 0:
        return ([1])
    for i in range(n-2):
        fibo.append(fibo[i]+fibo[i+1])
    return fibo