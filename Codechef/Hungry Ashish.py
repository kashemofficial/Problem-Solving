for _ in range(int(input())):
    m,p,b, = map(int,input().split())
    if p<m or (p == m):
        print('PIZZA')
    elif b<m or (b == m):
        print('BURGER')
    else:
        print('NOTHING')

