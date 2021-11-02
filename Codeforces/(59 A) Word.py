s = input()
l = len(s)
count = 0
for _ in s :
    if _ >= 'a' and _ <= 'z':
        count+=1
if count >= (l/2):
    print(s.lower())
else:
    print(s.upper())

