T = int(input())
for _ in range(T):
    X,N = map(int,input().split())
    if X > N:print("Invalid!")
    for j in range(1,N+1):
        D = X*j
        if D>N:
            break
        print(D)
    print()

'''
t = int(input())
for _ in range(t):
    x, n = map(int, input().split())
    if x > n: print("Invalid!")
    for i in range(1, n+1):
        mul = x*i
        if mul > n:break
        print(mul)
    print()
'''
























































































































