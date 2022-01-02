for _ in range(int(input())):
    n = int(input())
    li = list(map(int,input().split()))
    if sum(li)%2 == 1:
        print('YES')
    else:
        for i in range(len(li)):
            li[i] = li[i]%2

        if li.count(1)>0 and li.count(0)>0:
            print('YES')
        else:
            print('NO')



