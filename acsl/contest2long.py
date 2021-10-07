
# NORMAL SOLUTION:
# def rearrangedString(s):
#     s = [i for i in s if i.isalnum()]
#     charlist = set(s)
#     s = "".join(s)
#     occ = sorted(set([s.count(i) for i in charlist]))[::-1]
#     y = ["".join(sorted([j for j in charlist if s.count(j) == i])[::((occ.index(i) & 1) * -2 + 1)]) for i in occ]
#     z = dict(zip(occ, y))
#     fin = ",".join([str(i) + z[i] for i in z])
#     return str(fin)

# SUBMITTED CODE:
def rearrangedString(s):
    s = "".join([i for i in s if i.isalnum()])
    o = sorted(set([s.count(i) for i in set(s)]))[::-1]
    return ",".join(["".join(i) for i in zip([str(p) for p in o], ["".join(sorted([j for j in set(s) if s.count(j) == i])[::((o.index(i) & 1) * -2 + 1)]) for i in o])])
