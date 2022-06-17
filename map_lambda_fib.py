cube = lambda x: x**3

def fibonacci(n):
    fibo = [0, 1]
    for i in range(2, n):
        fibo.append(fibo[i-2]+fibo[i-1])
    return fibo[:n]
