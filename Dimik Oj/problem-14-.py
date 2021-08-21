T = int(input())
for i in range(T):
    string = input()
    charecter = input()
    if charecter in string:
        print("Occurrence of '%s' in '%s' ="%(charecter,string),(string.count(charecter)))
    else:
        print("'%s' is not present"%charecter)