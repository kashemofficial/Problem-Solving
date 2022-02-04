import math
for t in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = []
    x = a[0]
    for i in a:
        b.append((x*i)//math.gcd(x,i))
        x = i
    b.append(a[-1])
    print(b)
    

