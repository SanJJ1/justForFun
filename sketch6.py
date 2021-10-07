n = 1
z = []
while ((x := input()) != "0"):
    z.append(x)

print(z)
y = []
n = 0
p = "a"
for i in range(len(z) - 1):
    if z[i][0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        p = z[i]
    if z[i][0] in "abcdefghijklmnopqrstuvwxyz":
        n += 1
    else:
        y.append([p, n])
        n = 0
print(y)
