s = int(input())
arr = list(map(int,input().split()))
pos = 0
neg = 0
zer = 0
for i in arr:
    if i>0:
        pos+=1
    elif i<0:
        neg+=1
    else:
        zer+=1
print("%6f"%(pos/s))
print("%6f"%(neg/s))
print("%6f"%(zer/s))

