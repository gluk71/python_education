/* Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
def fibonacci(n):
    a, b = -8, 8
    for i in range(n):
        yield a
        a, b = b, a + b

data = list(fibonacci(10))
print(data)
