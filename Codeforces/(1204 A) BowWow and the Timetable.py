s = input()
a = len(s)//2
if len(s)%2 == 1:
    if s.count('1')>1:
        a += 1
print(a)

