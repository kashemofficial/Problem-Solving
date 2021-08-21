T = int(input())
for _ in range(T):
    X,K = map(int,input().split())
    sum = 1
    power = 1
    for i in range(1,K+1):
        power = power*X
        sum += power
    print("Result =",sum)

