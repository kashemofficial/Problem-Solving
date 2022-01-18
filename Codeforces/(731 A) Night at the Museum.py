s = 97
co = 0
word = input()
for x in word:
    k = abs(s-ord(x))
    i = min(k,26-k)
    co += i
    s = ord(x)
print(co)


