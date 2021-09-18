for t in range(int(input())):
    n = int(input())
    a = input().upper()
    li = ""
    for i in range(0,n):
        if (a[i] == 'L'):
            li += 'L'
        elif (a[i] == 'R'):
            li += 'R'
        elif (a[i] == 'U'):
            li += 'D'
        elif (a[i] == 'D'):
            li += 'U'
    print(li)








