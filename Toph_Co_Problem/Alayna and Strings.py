s = str(input())
l = 'abcdefghijklmnopqrstuvwxyz'
u = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
count_lower = 0
count_upper = 0

for i in s:
    if i in l:
        count_lower += 1
    elif i in u:
        count_upper += 1

print(count_upper,count_lower)