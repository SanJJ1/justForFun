# Construct a Numeral Hex Triangle according to the following rules:
# 1. The first row contains a starting hex number
# 2. Each of the next rows has one more number than the starting row.
# 3. Each number in the triangle is more than the previous number by a specified amount,
# given in Hex.
# one the triangles is constructed, find and print the sum of all the numbers on the last row.
# sum and re-sum digits until there's a single digit. Everything in Hex.
def sumOfLastRow(s, d, r):
    a = int(s, 16)
    b = int(d, 16)
    z = 0
    t = []
    for i in range(r):
        u = []
        for j in range(i + 1):
            u.append(hex(a + z * b))
            z += 1
        t.append(u)
    x = "".join(i[2:] for i in t[-1])
    while len(x) > 1:
        x = hex(sum(int(i, 16) for i in x))[2:]
    return x.upper()
print(sumOfLastRow("A", "9", 5))


# a = "ABC"
# b = "F"
#
# for i in range(10):
#     print(hex(int(a, 16) + i * int(b, 16)))