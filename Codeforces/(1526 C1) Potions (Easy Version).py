n = int(input())
a = list(map(int,input().split()))
arr = []
for i in range(n):
    arr.append(a[i])
    if sum(arr) < 0:
        arr.sort()
        arr.pop(0)
print(len(arr))

