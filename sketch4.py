x, y ,z = map(int, input().split())

x = x
y = max(y, x - y)
z = max(z, x - z)

print(y * z * 4)