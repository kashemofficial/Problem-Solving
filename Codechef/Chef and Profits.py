for _ in range(int(input())):
    a,b,c = map(int,input().split())
    res = (a*b)-(a*c)
    print(abs(res))