T = int(input())
for _ in range(T):
    import math
    N = int(input())
    def is_prime(N):
        for i in range(2,int(math.sqrt(N))):
            if N%i == 0:
                return False
        return True

    for i in range(1,N+1):
        if is_prime(i):
            print(i,"is a prime")
        else:
            print(i,"is not a prime")
'''
import sys
def prime(num):
    if num == 2:
        return True
    if num%2 == 0:
        return False
    for i in range(3, int(num**0.5)+1, 2):
        if num % i == 0:
            return False
    return True

Inputfile = sys.stdin
count = int(Inputfile.readline().strip())
for i in range(count):
    num = int(Inputfile.readline().strip())
    if prime(num):
        print("%d is a prime"%num)
    else:
        print("%d is not a prime"%num)
'''




'''
import sys
T = int(input())
for _ in range(T):
    num = int(input())
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print(num, "is not a prime")
                break
        else:
            print(num, "is a prime")
    else:
        print(num, "is not a prime")
'''