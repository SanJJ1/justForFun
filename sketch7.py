# n = int(input())
# s = 1
# for i in range(n):
#     s += int(input()) - 1
# print(s)

# x = input().split()
# z = []
# for i in x:
#     iter = 0
#     s = ""
#     while iter < len(i):
#         s += i[iter]
#         if i[iter] in "aeiou":
#             iter += 3
#         else:
#             iter += 1
#     z.append(s)
# print(" ".join(z))


x = int(input())
while x != -1:
    tp = 0
    su = 0
    for i in range(x):
        s, t = map(int, input().split())
        su += s * (t - tp)
        tp = t
    print(su, "miles")
    x = int(input())




