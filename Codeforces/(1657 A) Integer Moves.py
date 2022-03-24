import math
for t in range(int(input())):
    x, y = map(int,input().split())
    res = math.sqrt(x ** 2 + y ** 2)
    val = int(res)
    if x == 0 and y == 0:
        print(0)
    elif abs(res - val) == 0:
        print(1)
    else:
        print(2)
