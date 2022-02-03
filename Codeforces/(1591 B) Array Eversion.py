for t in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    mx = a[-1]
    c = 0
    for x in a[::-1]:
        if x > mx:
            mx = x
            c += 1
    print(c)




