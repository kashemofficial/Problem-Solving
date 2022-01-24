a = input()
c = 'AEIOUaeiou'
res = []
for i in a:
    if i in c:
        res.append(i)
print(len(res))
