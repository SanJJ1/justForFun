#1.  How many 6's are in the octal representation of the decimal numbers from 675 to 700, inclusive
# t = 0
# for i in range(675, 701):
#     print(i, oct(i))
#     t += oct(i).count('6')
# print(t) #11

#3.  Evaluate 13_16 * 74F_16 and return the answer in base16
# print(hex(16))
# a = 0x13
# b = 0x74F
# print(hex(a * b)) #0x8ADD

#3.  Find f(24), givern: [function]

# def f(x):
#     if x >= 10:
#         return x + f(x - 5)
#     if 5 < x < 10:
#         return f(x + 3) - 4
#     if x <= 5:
#         return 2 * x - 1
#
# print(f(24)) # 80

#4. Find f(3, 18), giverm: [function]
#
# def f(x, y):
#     if x > y:
#         return f(x - 2, y + 3) + 3
#     if x < y:
#         return f(y - 1, x + 1) - 5
#     else:
#         return x * y
# print(f(3, 18)) #143

#5. When this program is exectued, what is the largest value of any variable?
# 28

