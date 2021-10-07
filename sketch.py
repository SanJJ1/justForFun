
# 2d statues code

n = int(input())


import math
# for i in range(1,n + 1):
#     print(math.ceil(n/i) + math.ceil(math.log2(i)))


print(min([math.ceil(n/i) + math.ceil(math.log2(i)) for i in range(1, n + 1)]))

