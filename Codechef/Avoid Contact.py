for i in range(int(input())):
    x,y=map(int,input().split())
    if x==y:
        r=x+x-1
    else:
        r=x+y
    print(r)

