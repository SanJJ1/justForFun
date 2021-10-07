s = [int(i) for i in input().split()]
s.sort()

a = s[0]
b = s[1]
if s[2] == a + b:
    c = s[3]
else:
    c = s[2]
print(" ".join([str(a), str(b), str(c)]))