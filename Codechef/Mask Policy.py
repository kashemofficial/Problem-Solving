for _ in range(int(input())):
    a,b = map(int,input().split())
    if (a-b)>b:
        print(1)
    else:
        print(a-b)

