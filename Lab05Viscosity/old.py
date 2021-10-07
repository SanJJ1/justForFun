import csv
import math
import os
from scipy.stats import linregress
import matplotlib.pyplot as plt

# for file in os.scandir():
#     print(file.path[2:])

with open('Black_3.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    rows = [[i for i in row] for row in spamreader]

columns = list(zip(*rows[1:]))

header = rows[0]
n = 0
for i in columns[1]:
    if float(i) == 0:
        n += 1
times = [float(i) - float(columns[0][0]) for i in columns[0] if float(i) > 0][n:]
xs = [float(i) / 39.37 for i in columns[1] if float(i) != 0]
ys = [float(i) / 39.37 for i in columns[2] if float(i) != 0]

print(times)
print(xs)
print(ys)

x1 = xs[0]
y1 = ys[0]

d = [math.sqrt((ys[i] - y1)**2+(xs[i] - x1)**2) for i in range(len(xs))]
print(d)
result = linregress(times, d)
print(result.slope)
print("d300:",  d[50])


plt.figure()
plt.suptitle('Scatter plot')
plt.xlabel('a')
plt.ylabel('b')
plt.scatter(d, times, marker='.')


plt.show()