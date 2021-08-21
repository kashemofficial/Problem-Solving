import math
T = int(input())
for i in range(T):
    n = math.factorial(int(input()))
    count = 0
    while n>0:
        d = n % 10
        if d == 0:
            count+=1
            n = n//10
        else:
            break
    print(count)
    '''def count_zeros(x):
    i = 5
    zeros = 0
    while x >= i:
        zeros += x // i
        i *= 5
    return zeros

T = int(input(""))
for i in range(1, T+1):
	N = int(input(""))
	print(count_zeros(N))'''


    '''def fact(n):
    f = 1
    if n is 0 or n is 1: return 1
    for i in range(2, n+1):
        f *= i
    return f

def CountZero(f):
    count = 0
    while(f%10 == 0):
        count += 1
        f //= 10
    return count

for _ in range(int(input())):
    print(CountZero(fact(int(input()))))'''