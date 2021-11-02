a = input()
b = input()
count = 0
for i in range(0,len(a)):
    if a[i] == b[i]:
        count = '0'
    else:
        count = '1'
    print(count,end='')

