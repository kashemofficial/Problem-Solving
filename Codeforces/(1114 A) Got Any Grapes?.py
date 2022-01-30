x,y,z = map(int,input().split())
a,b,c = map(int,input().split())
if a>=x and a-x+b>=y and a-x+b-y+c >= z:
    print('YES')
else:
    print('NO')

