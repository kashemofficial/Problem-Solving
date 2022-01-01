T = int(input())
for i in range(T):
    count = 0
    S = input()
    vowels = "aeiou"
    for s in S:
        if s in vowels:
            count+=1
    if count > 0:
        print("Yes")
    else:
        print("No")

        