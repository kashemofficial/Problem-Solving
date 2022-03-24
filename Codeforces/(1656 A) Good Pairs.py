for t in range(int(input())):
    n = int(input())
    ar = list(map(int,input().split()))
    a = max(ar)
    b = min(ar)
    c = ar.index(a)+1
    d = ar.index(b)+1
    print(f"{d} {c}")

