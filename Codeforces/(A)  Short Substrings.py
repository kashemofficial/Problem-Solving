def Short_Substring(b):
    result = b[::2]+b[-1]
    print(result)
if __name__ == '__main__':
    for t in range(int(input())):
        b = input()
        Short_Substring(b)

