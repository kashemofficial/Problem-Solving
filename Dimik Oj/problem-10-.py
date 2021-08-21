t = int(input())
for i in range(1,t+1):
    r1,r2,b = map(int,input().split())
    CurrentRunRate = (r2/((300 - b)/6))
    RequerdRunRate = ((r1 - r2)+1)/(b/6)
    if r1 < r2:
        RequerdRunRate = 0.00
    print("%0.2lf %0.2lf"%(CurrentRunRate,RequerdRunRate))
