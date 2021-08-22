n1,n2,n3,n4 = map(float,input().split())
avr1 =((n1*2)+(n2*3)+(n3*4)+n4)/10
print('Media: %.1f'%avr1)
if avr1 >= 7.0:
    print('Aluno aprovado.')
elif avr1 < 5.0:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    e = float(input())
    print('Nota do exame: %.1f'%e)
    avr2 = (avr1+e)/2
    if avr2 >= 5.0:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print('Media final: %.1f'%avr2)
