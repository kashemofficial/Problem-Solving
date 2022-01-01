word = input()
res = word.replace('s', '$').replace('i', '!').replace('o', '()')
print(res.capitalize(),end='.')