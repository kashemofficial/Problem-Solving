import math
T = int(input())
for i in range(T):
    N = int(input())
    A = int(math.sqrt(N))
    if A*A==N:
        print("YES")
    else:
        print("NO")