def countArray(n, k, x):
    M = 1000000007
    Pi = 0 if x == 1 else 1
    Ti = k - 1
    for i in range(2, n):
        Pi = (Ti - Pi) % M
        Ti = Ti * (k - 1) % M
    return Pi
if __name__ == '__main__':
    first_multiple_input = input().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    x = int(first_multiple_input[2])
    answer = countArray(n, k, x)
    print(answer)
