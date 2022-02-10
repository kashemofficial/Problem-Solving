for t in range(int(input())):
    a,b,c = map(int,input().split())
    s1 = a+b
    s2 = a+c
    while s2 <= s1:
        s2 += c
    print("Case %d: %d"%(t+1,s2))

