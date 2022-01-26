for _ in range(int(input())):
    a,b,c= map(int,input().split())
    if (b*3)-(a-b)>=c:
        print('PASS')
    else:
        print('FAIL')
