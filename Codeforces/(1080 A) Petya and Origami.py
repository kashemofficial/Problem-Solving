import math
n,k = map(int,input().split())
res1 = math.ceil(n*8/k)
res2 = math.ceil(n*5/k)
res3 = math.ceil(n*2/k)
print(res1+res2+res3)
