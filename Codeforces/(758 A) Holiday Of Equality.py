n = int(input())
arr = list(map(int,input().split()))
m = max(arr)
a = 0
for i in arr:
    a = a+(m-i)
print(a)

