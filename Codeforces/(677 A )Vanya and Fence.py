a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = 0
for i in b:
    if i > a[1]:
        c+=2
    else:
        c+=1
print(c)


