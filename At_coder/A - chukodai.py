s = str(input())
a,b = map(int,input().split())
co = []
for i in s:
    co.append(i)

co[a-1],co[b-1] = co[b-1],co[a-1]
print(*co,sep='')

