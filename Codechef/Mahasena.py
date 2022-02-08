n = int(input())
arr = list(map(int,input().split()))
c_e = 0
c_o = 0
for i in arr:
    if i%2 == 0:
        c_e+=1
    else:
        c_o+=1
if c_e>c_o:
    print('READY FOR BATTLE')
else:
    print('NOT READY')

