s=input()
l=[]
for c in s:
    l.append(c)
print(max(l,key=l.count))

