for _ in range(int(input())):
    a,b,c = map(float,input().split())
    result = ((a/10)*2+(b/10)*3+(c/10)*5)
    print('%.1f'%result)
