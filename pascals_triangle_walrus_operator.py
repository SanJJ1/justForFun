# Author: Raymond Hettinger @raymondh on Twitter
#

def binom(n):
    'Coefficients of (x + 1) ** n'
    return [(c := c * (n - k + 1) // k if k else 1) for k in range(n + 1)]


for i in range(10):
    print(" ".join([str(i) for i in binom(i)]))
