l = [1,2,3,4,5,6,7]
for t in range(int(input())):
    n = int(input())
    ara = list(map(int,input().split()))
    s = 0
    for i in range(n):
        if ara[i] in l:
            s += 1
        if s == 7:
            print(i)
            break

