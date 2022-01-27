for t in range(int(input())):
    n,m = map(int,input().split())
    for i in range(n):
        m = m*(m+1)//2
    print(m)
