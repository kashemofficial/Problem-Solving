for _ in range(int(input())):
    a = int(input())
    if (a>0):
        if a%2==0:
            print('EVEN POSITIVE')
        else:
            print('ODD POSITIVE')

    elif (a<0):
        if a%2 == 0:
            print('EVEN NEGATIVE')
        else:
            print('ODD NEGATIVE')
    else:
        print('NULL')


        




