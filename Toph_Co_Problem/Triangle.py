import math
for _ in range(int(input())):
    a,b,c = map(int,input().split())
    s = (a+b+c)/2
    Area = (s*(s-a)*(s-b)*(s-c))
    if (Area < 0):
        print('Oh, No!')
    else:
        print('%.2f'%math.sqrt(Area))

