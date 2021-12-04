x = 0
for i in range(int(input())):
    n = input()
    if n[0] == '+' or n[1] == '+':
        x += 1
    elif n[0] == '-' or n[1] == '-':
        x -= 1
print(x)
