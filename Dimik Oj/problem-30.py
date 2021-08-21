T = int(input())
import math
for i in range(T):
    N = int(input())
    sq,sum = int(math.sqrt(N)),1
    for i in range(2,sq+1):
        if N%i == 0:
            sum += (N//i) + i
        if sum>N:
            break
    if sum == N:
        print("YES, {} is a perfect number!".format(N))
    else:
        print("NO, {} is not a perfect number!".format(N))









"""t = int(input())
import math
for _ in range(t):
    n = int(input())
    sq, sum = int(math.sqrt(n)), 1
    for i in range(2, sq):
        if n % i == 0:
            sum += i
            sum += (n//i)
        if sum > n:
            break
    if n % sq == 0:
        sum += sq
        val = n // sq
        if val != sq:
            sum += val
    if sum == n:
        print("YES, {} is a perfect number!".format(n))
    else:
        print("NO, {} is not a perfect number!".format(n))
        """
t = int(input())
import math
for _ in range(t):
    n = int(input())
    sq, sum = int(math.sqrt(n)), 1
    for i in range(2, sq+1):
        if n % i == 0:
            sum += (n//i) + i
        if sum > n:
            break
    if sum == n:
        print("YES, {} is a perfect number!".format(n))
    else:
        print("NO, {} is not a perfect number!".format(n))