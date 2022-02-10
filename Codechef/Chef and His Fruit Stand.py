try:
    for t in range(int(input())):
        x,y = map(int,input().split())
        if (x/2 <= y):
            print(int(x/2))
        else:
            print(int(y))
except:
    pass

