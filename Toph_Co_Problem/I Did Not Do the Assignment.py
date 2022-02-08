N = int(input())
if N>1:
    for i in range(2,N):

        if N%i == 0:
            for i in range(N):
                print("I DID NOT DO THE ASSIGNMENT.")
            break
    else:
        print("NO PUNISHMENT")
