import math
T=int(input())
for i in range(T):
    a,b,c=list(map(int,input().split()))
    s=(a+b+c)/2
    Area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("Area = %0.3f"%Area)

