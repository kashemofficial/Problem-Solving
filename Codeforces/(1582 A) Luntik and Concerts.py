for t in range(int(input())):
    a,b,c = map(int,input().split())
    if (a+b*2+c*3)%2 == 0:
        print(0)
    else:
        print(1)

