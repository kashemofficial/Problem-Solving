a,b,c,d = map(int,input().split())
ans = -1
res= c*d-b
if 0 < res:
    ans = (a+res-1)//res
print(ans)
