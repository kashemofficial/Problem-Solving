t = int(input())
for i in range(t):
    n = int(input())
    sum = 0
    A = n #intput ta ka A a rakha hoica
    while A > 0:#0 thaka A bor
        D = A % 10#last sonka bahir kora hoica
        sum += D ** 3 #D ar upor a quabe dawa hoica
        A //= 10 #float sonka jano na asa tar last sonka niba
    if n == sum:
        print(n,"is an armstrong number!")
    else:
        print(n,"is not an armstrong number!")