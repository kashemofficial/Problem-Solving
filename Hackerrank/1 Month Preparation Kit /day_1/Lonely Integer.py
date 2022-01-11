a = int(input())
b = map(int,input().split())
res = 0
for i in b:
    res ^= i
print(res)
