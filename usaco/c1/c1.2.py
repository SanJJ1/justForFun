n = int("4")
s = [int(i) for i in "1 1 2 3".split()]
np = n

for i in range(n):
    for j in range(i + 1, n):
        if (sum(s[i:j + 1])/(j-i + 1)) in s[i:j + 1]:
            np += 1
            # print(i, j, (sum(s[i:j + 1])/(j-i + 1)), s[i:j + 1])

print(np)