def f(x, y):
    return (x + y + x * y) / (2 ** x * (2 ** x + 2 ** y))


for i in range(100):
    s = 0
    for m in range(i):
        for n in range(i):
            s += f(m, n)

    print(s)
