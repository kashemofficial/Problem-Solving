T = int(input())
for i in range(1,T+1,1):
    N = (list(map(int,input().split())))
    N.sort()
    print("Case %d:"%i,*N)