from math import pi
from numpy import log as ln

g = 9.81
rc = 0.0061
lc = 0.038
mc = 0.038
rt = 0.0080

vf1 = 350
vf2 = 1000

pf = 970
vc = pi * rc * rc * lc
phi = lc/rc

pc = mc/vc

k = rc/rt

cw = 1.003852 - 1.961019 * k + 0.9570952 * k ** 2

gk = (k * k * (1 - ln(k)) - (1 + ln(k))) / (1 + k * k)

ecf = 1 / (1 +(8 * k / (pi * cw)) * (gk / phi))

vt = [0.0317, 0.00987, 0.0024]

fluidNum = 0
muf = (g * rc * rc * (pc - pf) * gk * ecf) / (2 * vt[fluidNum])

vttech = (g * rc * rc * (pc - pf) * gk) / ((2 * vt[fluidNum]) / ecf)

cst = 1E-6
vfk = (muf / pf) / cst

ac = pi * rc * rc
at = pi * rt * rt

P = 2 * pi * (rc + rt)

L = 4 * (at - ac) / P

vfavg = vt[fluidNum] * ac / (at - ac)

re = L * vfavg * pf / muf
print("gk", gk)
print("cw", cw)
print("ecf", ecf)
print("muf", muf)
print("vfk", vfk)
print("re", re)

print("vfavg", vfavg)
