def fibonacci(n):
    x = 0
    y = 1
    hichem = []
    while x < n:
        hichem.append(x)
        x, y = y, x + y
        print(hichem)

fibonacci(111)


# def math(x):
#     x = 0
#     y = x * x
#     x = y
# math(5)
