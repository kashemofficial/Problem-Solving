def __even__odd__(n):
    if n%2 != 0 or n > 5 and n<21:
        print('Weird')
    else:
        print('Not Weird')
if __name__ == '__main__':
    while True:
        n = int(input().strip())
        __even__odd__(n)

