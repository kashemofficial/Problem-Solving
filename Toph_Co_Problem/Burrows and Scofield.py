s1 = str(input())
s2 = str(input())
a = '0123456789'
co = []
a1 = 0
a2 = 0
a3 = 1
for i in s1:
    if i in a:
        co.append(int(i))
for j in s2:
    if j in a:
        co.append(int(j))

for k in co:
    a1+=k
    a2-=k
    a3*=k
result = abs(min(a1,a2,a3))
print(f'"{result}"')




