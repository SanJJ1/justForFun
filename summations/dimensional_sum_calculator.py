from scipy.special import comb

# 2 dimensions
# a = 29
# b = 11
# c = 17
# i = list(range(1, a + 1))
# j = list(range(1, b + 1))
# k = list(range(1, c + 1))
# sum = 0
# for it in i:
#     for jt in j:
#         for kt in k:
#             sum += it * jt * kt
#
# print(sum, a * b * c * (a+1) * (b+1) * (c+1)/ 8)

# 3 dimensions
a = 17
b = 11
i = list(range(1, a + 1))
j = list(range(1, b + 1))
sum = 0
for it in i:
    for jt in j:
        sum += it * jt

print(sum, a * b * (a+1) * (b+1)/ 4)

print(comb(a + 1, 2) * comb(b + 1, 2))

