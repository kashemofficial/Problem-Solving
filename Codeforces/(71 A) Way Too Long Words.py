for t in range(int(input())):
    n = input()
    if len(n)<=10:
        print(n)
    elif len(n) > 10:
        print(f'{n[0]}{len(n[1:-1])}{n[-1]}')

