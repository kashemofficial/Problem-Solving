k,l = map(int,input().split())
a = {int(x) for x in input().split()}
b = {int(y) for y in input().split()}
c = a.union(b)
d = sorted(c)
print(*d)
