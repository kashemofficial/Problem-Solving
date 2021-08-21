a0,a1,a2 = map(int,input().split())
b0,b1,b2 = map(int,input().split())
_alice = [a0,a1,a2]
_bob = [b0,b1,b2]
sc = [0,0]
for a,b in zip(_alice,_bob):
    if a > b:
        sc[0]+=1
    elif b > a:
        sc[1]+=1
print(*sc)