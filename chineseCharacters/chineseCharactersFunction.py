# instructions:
# input your code to be shrinked into variable x
# take the printed output from y, and put it into z.
# you may have to truncate the code to make it work.
# take the output, then put it into:
# [output]','u16')[2:])

x = """rows = len(grid)
col = len(grid[0])
p = 0
for i in range(rows):
    for j in range(col):
        if grid[i][j]:
            if not i:
                 p += 1
            elif not grid[i - 1][j]:
                p += 1
            if i + 1 == rows:
                p += 1
            elif not grid[i + 1][j]:
                p += 1

            if not j:
                p += 1
            elif not grid[i][j - 1]:
                p += 1
            if j + 1 == rows:
                p += 1
            elif not grid[i][j + 1]:
                p += 1
    return p"""
y = bytes(x, 'u8')
# for i in y:
#     print(i)
# print(y)
print(y.decode('u16'))



# z = b'print(sum([ord(i)if ord(i)& 1 else ord(i)*2 for i in input()]))\n'
print(f"exec(bytes('{y.decode('u16')}','u16')[2:])")


# w=input()
# print([" ","\n"][input()!='S'].join(w[::(i&1)*-2+1] for i in range(len(w))))