t = int(input())
li = list(map(int,input().split()))
low = li[0]
hig = li[0]
low_score = 0
high_score = 0
for i in li:
    if i < low:
        low = i
        low_score += 1
    elif i > hig:
        hig = i
        high_score += 1
print(high_score,low_score)
