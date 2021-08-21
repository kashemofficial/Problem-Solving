T = int(input())
for i in range(T):
    N = int(input())
    C = N % 10  # c = last digit
    while N > 0:
        S = N%10 # s=last digit
        N = N // 10  # N = frist desit bahir kora
        if (N < 10):
            print("sum = %d" % (C + N))
            break

"""T = int(input())
for _ in range(T):
    Number = int(input())
    firstNumber = Number // 10000
    lastNumber  = Number % 10
    result = firstNumber+lastNumber
    print('Sum =',result)"""
