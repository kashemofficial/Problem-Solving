T = int(input())
for i in range(T):
    ch = input()
    if (ch>="a" and ch<="z"):
        print("Lowercase Character")
    elif (ch>="A" and ch<="Z"):
        print("Uppercase Character")
    elif (ch>="0" and ch<="9"):
        print("Numerical Digit")
    else:
        print("Special Character")