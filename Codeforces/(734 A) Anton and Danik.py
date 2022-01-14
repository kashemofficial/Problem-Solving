n = int(input())
a = input()
a1 = 0
a2 = 0
for i in a:
    if i == 'A':
        a1+=1
    elif i == 'D':
        a2+=1

if a1 > a2:
    print('Anton')
elif a1 == a2:
    print('Friendship')
else:
    print('Danik')