n = int(input())
c = 0
arr={4,7,47,74,44,444,447,474,477,777,774,744}
for i in arr:
    if(n%i==0):
        c = True
if c:
    print("YES")
else:
    print("NO")

'''n = int(input())
if (n%4==0):
    print('YES')
elif(n%7==0):
    print('YES')
elif (n%44==0):
    print('YES')
elif (n%47==0):
    print('YES')
elif (n%74==0):
    print('YES')
elif (n%77==0):
    print('YES')
elif (n%444==0):
    print('YES')
elif (n%447==0):
    print('YES')
elif (n%474==0):
    print('YES')
elif (n%477==0):
    print('YES')
elif (n%744==0):
    print("YES")
elif (n%747==0):
    print('YES')
elif (n%774==0):
    print('YES')
elif (n%777==0):
    print('YES')
else:
    print('NO')'''
