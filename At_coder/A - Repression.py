a,b,c = map(int,input().split())
result = a,b,c
co = 0
res = min(a,b,c)
for i in result:
    co += i
print(co-res)

