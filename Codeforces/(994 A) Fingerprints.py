a,b=input().split()
l1=input().split()
l2=input().split()
res=[]
for i in l1:
    if i in l2:
        res.append(i)
print(*res)


