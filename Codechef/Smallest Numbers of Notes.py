for _ in range(int(input())):
    n = int(input())
    a = 0
    a+=n//100
    n %= 100
    a+=n//50
    n %= 50
    a+=n//10
    n %= 10
    a+=n//5
    n %= 5
    a+=n//2
    n %= 2
    a+=n//1
    n %= 1
    print(n)
