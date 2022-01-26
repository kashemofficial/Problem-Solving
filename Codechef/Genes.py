a,b = input().split()
if a == 'R' or b == 'R':
    print('R')
elif a == 'G':
    print(b)
elif b == 'G':
    print(a)
elif a == b:
    print(a)

