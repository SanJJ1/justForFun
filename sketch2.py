s = "4 1"

n, k = [int(i) for i in input().split()]

attacks = []
damages = []
healths = []
for j in range(n):
    x = [int(i) for i in input().split()]
    attacks += [[j, x[0]]]
    damages += [[j, x[1]]]
    healths += [[j, x[2]]]

attacks.sort(key=lambda i:-i[1])
damages.sort(key=lambda i:-i[1])
healths.sort(key=lambda i:-i[1])

attacks = attacks[:k]
damages = damages[:k]
healths = healths[:k]

z = []
for i in range(k):
    z += [attacks[i][0],damages[i][0], healths[i][0]]


print(len(set(z)))
