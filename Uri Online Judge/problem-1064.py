for i in range(int(input())):
    n = int(input())
    result = 0
    for i in range(1,n):
        if n % i == 0:
            result += i
    if result == n:
        print('%d eh perfeito'%n)
    else:
        print('%d nao eh perfeito'%n)
