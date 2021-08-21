T = int(input())
for i in range(T):
    N=int(input())
    fact=1
    if (N<0):
        print()
    else:
        for i in range(1,N+1):
            fact=fact*i
        print(fact)
