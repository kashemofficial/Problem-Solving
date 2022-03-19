a,b = map(int,input().split())
ara1 = set(list(map(int,input().split())))
ara2 = set(list(map(int,input().split())))
if len(ara1 & ara2):
    print(min(ara1 & ara2))
else:
    c,d = sorted((min(ara1),min(ara2)))
    print(str(c)+str(d))
