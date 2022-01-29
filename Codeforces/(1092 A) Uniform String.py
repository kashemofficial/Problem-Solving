arr = "abcdefghijklmnopqrstuvwxyz"
for i in range(int(input())):
    n, k = map(int, input().split())
    for j in range(n):
        print(arr[j % k], end="")
    print()




