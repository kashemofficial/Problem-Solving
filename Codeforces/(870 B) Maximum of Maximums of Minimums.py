a,b = map(int,input().split())
ara = list(map(int,input().split()))
if b == 1:
    print(min(ara))
elif b == 2:
    print(max(ara[0],ara[-1]))
else:
    print(max(ara))























