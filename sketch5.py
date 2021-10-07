n = int(input())
while(n != 0):
    x = []
    for i in range(n):
        x.append(input())
    x.sort(key=lambda j:j[:2])
    for i in x:
        print(i)
    n = int(input())
    if n == 0:
        exit()
    print("")
