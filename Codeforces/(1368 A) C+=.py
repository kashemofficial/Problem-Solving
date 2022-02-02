for t in range(int(input())):
    a,b,n = map(int,input().split())
    ans = 0
    while max(a, b) <= n:
        ans += 1
        if a > b:
            b += a
        else:
            a += b
    print(ans)