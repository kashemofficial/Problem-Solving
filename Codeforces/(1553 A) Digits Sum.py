for t in range(int(input())):
    n = int(input())
    result = n/10
    if n%10 == 9:
        result+=1
    print(int(result))


