for t in range(int(input())):
    a,b = map(int,input().split())
    if a>b:
        print(abs(a-b))
    elif a%2 == b%2:
        print(0)
    else:
        print(1)

