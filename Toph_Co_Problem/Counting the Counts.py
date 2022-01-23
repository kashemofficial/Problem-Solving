n = int(input())
arr = list(map(int,input().split())) [:n]
co = 0
for i in arr:
    if i <= 100 and i >= 80:
        co += 1
print(co)
