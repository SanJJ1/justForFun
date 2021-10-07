z = """6
E 3 5
N 5 3
E 4 6
E 10 4
N 11 2
N 8 1""".split("\n")[1:]
cows = []


class Cow:
    def __init__(self, dir, x, y):
        self.dir = "N" == dir
        self.x = int(x)
        self.y = int(y)
        self.ce = 0
        self.stopped = False

    def __str__(self):
        return f"{self.ce} | {['E', 'N'][self.dir]} | {self.x} | {self.y} | {self.stopped}\n"

    def __repr__(self):
        return self.__str__()


for i in z:
    c = Cow(*i.split())
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
