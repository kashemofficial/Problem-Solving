"""T = int(input())
for i in range(T):
    S = input()
    A = S.replace("","")
    D = A[::-1]
    if A == D :
        print("Yes! It is Palindrome!")
    else:
        print("Sorry! It is not Palindrome!")
        """
t = int(input())
for i in range(t):
    s = input()
    if s == s[::-1]:
        print("Yes! It is Palindrome!")
    else: 
        print("Sorry! It is not Palindrome!")