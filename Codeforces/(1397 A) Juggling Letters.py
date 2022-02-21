for t in range(int(input())):
    n = int(input())
    arr = ''
    for _ in range(n):
        arr += str(input())
    c = 0
    for i in set(arr):
        if arr.count(i)%n != 0:
            c+=1
    if c == 0:
        print('YES')
    else:
        print('NO')








