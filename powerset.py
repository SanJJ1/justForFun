import pprint as pp


x = list(range(8))


def ps(s):
    l = []
    x = len(s)
    for i in range(1 << x):
        l.append([s[j] for j in range(x) if (i & (1 << j))])
    return l

final = ps(x)
final.sort(key=lambda y: len(y))
pp.pprint(final)
