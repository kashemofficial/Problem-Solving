for _ in range(int(input())):
    n = int(input())
    for i in range(2,n):
        if (n%i == 0):
            print('%d nao eh primo'%n)
            break
    else:
        print('%d eh primo'%n)