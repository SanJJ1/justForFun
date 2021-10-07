# This is a script that is extremely inefficient, and uses recursion
# rather than iteration to sum a linearly increasing sequence of values,
# where the different between one value and the next is 1
# Examples: 1 + 2 + 3 + 4 + 5,
# 14 + 15 + 16 + 17 + 18


for i in range(2, 10):
    x = list(range(1, i))
    print(sum(x))


def sum2(n):
    if n > 1:
        return sum2(n // 2) * 2 + ((n + 1) // 2) ** 2
    return 1

for i in range(10):
    print(sum2(i))