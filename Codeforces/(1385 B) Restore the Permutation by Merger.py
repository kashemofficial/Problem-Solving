for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    co = []
    for i in arr:
        if i not in co:
            co.append(i)
    print(*co,sep=' ')

