"""T = int(input())
for i in range(T):
    N = input().lower()
    vowel = {"a","e","i","o","u"}
    for i in N:
        if i in vowel:
            print(i,end="")
    print()
    for j in N:
        if j in vowel:
            continue
        print(j.replace(" ",""),end="")
    print()"""
n = int(input())
for i in range(n):
    s = input()
    vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    v,c = '', ''
    for ch in s:
        if (ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z'):
            if ch in vowel:
                v += ch
            else:
                c += ch
    print(v)
    print(c)
'''for i in range(int(input())):
    string = input()
    vowel, consonant = '', ''
    for s in string:
        if s is 'a' or s is 'e' or s is 'i' or s is 'o' or s is 'u' or s is 'A' or s is 'E' or s is 'I' or s is 'O' or s is 'U':
            vowel += s
        elif s >= 'b' and s <= 'z' or s >= 'B' and s <= 'Z':
            consonant += s

    print(vowel, consonant, sep='\n')'''



