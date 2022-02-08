x,y = map(int,input().split())
temp = y
while 1:
    if y%x == 0:
        break
    y+=1
print(y-temp)

