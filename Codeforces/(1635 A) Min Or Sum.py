for t in range(int(input())):
    n = int(input())
    ara = list(map(int,input().split()))
    ans = 0
    for i in ara:
        ans = ans | i
    print(ans)

