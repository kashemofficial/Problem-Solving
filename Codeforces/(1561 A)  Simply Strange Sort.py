def is_sorted(a):
    return all(a[i] < a[i+1] for i in range(len(a)-1))

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0
    while not is_sorted(a):
        for i in range(ans%2,n-1,2):
            if a[i]>a[i+1]:
                a[i],a[i+1] = a[i+1],a[i]
        ans += 1
    print(ans)







