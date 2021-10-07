class Cow:
    def __init__(self, dir, x, y):
        self.dir = "N" == dir
        self.x = int(x)
        self.y = int(y)
        self.ce = 0
        self.stopped = False


cows = []
n = int(input())
for i in range(n):
    c = Cow(*input().split())
    cows.append(c)

ec = []

ctag = cows.copy()
for i in range(120):
    dirs = [j.dir for j in ctag]

    for c in ctag:
        ec.append((c.x, c.y))
        c.ce += 1
        if c.dir:
            c.y += 1
        else:
            c.x += 1
    # if all(dirs) or not any(dirs):
    #     for j in ctag:
    #         j.ce = "Infinity"
    #     ctag = []
    for j in ctag:
        if (j.x, j.y) in ec:
            ctag.remove(j)


for c in cows:
    if c.ce > 100:
        print("Infinity")
    else:
        print(c.ce)