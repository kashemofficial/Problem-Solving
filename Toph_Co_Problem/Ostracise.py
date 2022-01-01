or _ in range(int(input())):
    n = int(input())
    li = list(map(int,input().split())) [:n]
    res = []
    for i in sorted(li):
        if li[0] != i:
            res.append(i)
    for i in res:
        print(i)
