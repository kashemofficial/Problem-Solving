n = int(input())
arr = list(map(int,input().split()))
a = [0]*100
for i in arr:
    a[i] += 1
print(*a)
