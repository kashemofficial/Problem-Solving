T = int(input())
for _ in range(T):
    try:
        a,b = map(int,input().split())
        print(a//b)
    except Exception as e:
        print("Error Code:",e)


