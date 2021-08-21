T = int(input())
for i in range(T):
    a = input()
    b = a.lower()
    count = 0
    li = ['a', 'e', 'i', 'o', 'u']
    for i in b:
        if i in li:
            count = count + 1
    print("Number of vowels =",count)
'''for i in range(int(input())):
    s = input()
    NumberOfVowel = s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u') + s.count('A') + s.count('E') + s.count('I') + s.count('O') + s.count('U')
    print("Number of vowels = {}".format(NumberOfVowel))'''


