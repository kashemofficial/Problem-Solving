for t in range(int(input())):
    a,b,c = map(int,input().split())
    res1 = b//c
    res2 = b%c
    if a//c == res1:
        print(res2+res1)
    else:
        print(max(res1+res2,res1+c-2))
