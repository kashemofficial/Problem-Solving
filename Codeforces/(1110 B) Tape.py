n,m,w = map(int,input().split())
arr = list(map(int,input().split()))
k = []
for i in range(1,n):
    a = arr[i] - arr[i-1]
    k.append(a)
k.sort()
s = 0
for i in range(n-w):
    s+=k[i]
print(s+w)
