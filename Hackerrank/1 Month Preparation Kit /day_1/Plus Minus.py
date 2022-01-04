n = int(input())
a = list(map(int,input().split()))
pos = 0
neg = 0
zer = 0
for i in a:
    if i>0:
        pos+=1
    elif i<0:
        neg+=1
    else:
        zer+=1
#print(f"{pos/len(a):6f}\n{neg/len(a):6f}\n{zer/len(a):6f}")
print('%6f'%(pos/len(a)))
print('%6f'%(neg/len(a)))
print('%6f'%(zer/len(a)))


