a,b = list(map(int,input().split()))
if a<b:
    a,b = b,a
k = 0
while (a != 0 and b != 0):
    k+= a//b
    a = a%b
    a,b = b,a
print(k)
