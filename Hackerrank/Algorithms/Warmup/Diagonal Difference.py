n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
sum = len(arr)
l = r = 0
for i in range(sum):
    l += arr[i][i]
    r += arr[i][sum - i - 1]
print(abs(l - r))

