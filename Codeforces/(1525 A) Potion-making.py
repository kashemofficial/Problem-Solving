import math
for _ in range(int(input())):
    k = int(input())
    n = math.gcd(k,100-k)
    x = k/n
    y = (100 - k)/n
    print(int(x+y))