n,a,b = map(int,input().split())
arr = list(map(int,input().split()))
count = 0
for i in arr[a:b+1]:
    count += i
print(count)

