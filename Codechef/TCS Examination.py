T = int(input())
while (T > 0):
    a, b, c = map(int, input().split())
    x, y, z = map(int, input().split())
    dragon = a + b + c
    sloth = x + y + z
    if (dragon > sloth):
        print("Dragon")
    elif (sloth > dragon):
        print("Sloth")
    else:
        if (sloth == dragon):
            if (a > x):
                print("Dragon")
            elif (x > a):
                print("Sloth")
            else:
                if (b > y):
                    print("Dragon")
                elif (y > b):
                    print("Sloth")
                else:
                    print("Tie")

    T -= 1