a,b = map(int,input().split())
if a<b:
    print('O JOGO DUROU %d HORA(S)'%(b-a))
else:
    print('O JOGO DUROU %d HORA(S)'%(b+24-a))


