for t in range(int(input())):
    n = int(input())
    a = n//3
    b = n//3
    co = n%3
    if co == 1:
        print(a+1,b)
    elif co == 2:
        print(a,b+1)
    else:
        print(a,b)




