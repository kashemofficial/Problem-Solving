def Cherry(n,a):
    ans = a[0]*a[1]
    for i in range(1,n-1):
        ans = max(ans,a[i]*a[i-1],a[i]*a[i+1])
    print(ans)
if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int,input().split()))
        Cherry(n,a)

'''a = [719313,273225,402638,473783,804745,323328]
print(273225*719313 , 273225*402638)
print(402638*273225 , 402638*473783)
print(473783*402638 , 473783*804745)
print(804745*473783 , 804745*323328)'''



'''t = int(input())
while t!= 0:
    t -= 1
    n = int(input())
    a = list(map(int,input().split()))
    result = a[0]*a[1]
    for i in range(1,n-1):
        result = max(result,a[i]*a[i-1],a[i]*a[i+1])
    print(result)'''
