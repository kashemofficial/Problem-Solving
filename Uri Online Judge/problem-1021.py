valor = float(input())
notas = [100, 50, 20, 10, 5, 2]
modas = [1, 0.50, 0.25, 0.10, 0.05 , 0.01]
print("NOTAS:")
for nota in notas:
    note = int(valor/nota)
    print("{} nota(s) de R$ {:.2f}".format(note,nota))
    valor -= note * nota
print("MOEDAS:")
for moda in modas:
    mode = int(round(valor,2)/moda)
    print("{} moeda(s) de R$ {:.2f}".format(mode,moda))
    valor -= mode * moda
