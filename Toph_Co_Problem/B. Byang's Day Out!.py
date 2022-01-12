for _ in range(int(input())):
    x,y,z = map(int,input().split())
    if (x+y>=z and x+z>=y and y+z>=x) :
        print('Yes')
    else:
        print('No')