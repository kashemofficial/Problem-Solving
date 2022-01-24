s = input()
c1 = 0
c2 = 0
c3 = 0
for i in s:
    if i == 'Q':
        c1 += 1
        c3 += c2
    elif i == 'A':
        c2 += c1
print(c3)