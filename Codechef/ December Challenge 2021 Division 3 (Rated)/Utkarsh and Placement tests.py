try:
    for _ in range(int(input())):
        a,b,c = map(str,input().split())
        a1,b1  = map(str,input().split())
        if a == a1:
            print(a1)
        elif a == b1:
            print(b1)
        elif b == a1:
            print(a1)
        else:
            print(b1)
except:
    pass
