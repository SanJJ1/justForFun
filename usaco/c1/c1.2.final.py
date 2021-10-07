n = int(input())
s = [int(i) for i in input().split()]
np = n

for i in range(n):
    for j in range(i + 1, n):
        if (sum(s[i:j + 1])/(j-i + 1)) in s[i:j + 1]:
            np += 1
print(np)