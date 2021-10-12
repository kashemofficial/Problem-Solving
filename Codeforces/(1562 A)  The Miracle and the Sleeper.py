for _ in range(int(input())):
    l,r = list(map(int,input().split()))
    MOD = max(l,(r//2)+1)
    print(r%MOD)

