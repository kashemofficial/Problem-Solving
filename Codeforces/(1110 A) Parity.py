n,k = map(int,input().split())
a = list(map(int,input().split()))
r = sum(a[:-1]*n,a[-1])
if r%2 == 0:
    print('even')
else:
    print('odd')

    