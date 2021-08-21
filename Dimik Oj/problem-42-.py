T = int(input())
for i in range(T):
    n = int(input())
    for j in range(n,-1,-1):
        if j == 1:
            print("2 + ",end="")
        elif j == 0:
            print("1",end="")
        else:
            print("2^%d + "%j,end="")
    print()



