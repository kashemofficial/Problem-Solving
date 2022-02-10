for t in range(int(input())):
    a,b = map(int,input().split())
    c = a-b
    ans = 0
    if a == b:
        ans = 0
    elif c>=0:
        if c%2 == 0:
            ans+=1
        else:
            ans+=2
    else:
        if c%2 != 0:
            ans += 1
        else:
            ans += 2
    print(ans)

