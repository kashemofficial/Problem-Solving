t = int(input())
for i in range(t):
    string = input().split()
    length = len(string)
    for index in range(0, length):
        if index == length - 1:
            print(string[index][::-1])
        else:
            print(string[index][::-1], end=' ')
