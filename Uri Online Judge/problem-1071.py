x = int(input())
y = int(input())
c = 0
for i in range(y+1,x):
    if i%2 == 1:
        c+=i
print(c)
