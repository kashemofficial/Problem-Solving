for _ in range(int(input())):
    a,b,c = map(int,input().split())
    res = a,b,c
    ans = sorted(res)
    print(ans[1])

