for t in range(int(input())):
    n = int(input())
    ara = list(map(int,input().split()))
    c = 0
    for i in range(len(ara)):
        if ara[i]%2 == 0:
            c += 1
    if c == n:
        print('Yes')
    else:
        print('No')
