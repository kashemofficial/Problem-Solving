for t in range(int(input())):
    n,k=map(int,input().split())
    a,b=[[*map(int,input().split())] for i in range(2)]
    for i,j in sorted(zip(a,b)):
        if k-i<0:
            break
        k+=j
    print(k)

