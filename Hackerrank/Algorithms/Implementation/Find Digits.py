for _ in range(int(input())):
    n = int(input())
    count = 0
    for i in str(n):
        try:
            if n%int(i) == 0:
                count+=1
        except ZeroDivisionError:
            pass
    print(count)




