even = 0
odd = 0
positive = 0
negative = 0
for i in range(5):
    n = int(input())
    if n%2 == 0:
        even+=1
    else:
        odd += 1
    if 0<n:
        positive+=1
    if 0>n:
        negative+=1
print(f"{even} valor(es) par(es)")
print(f"{odd} valor(es) impar(es)")
print(f"{positive} valor(es) positivo(s)")
print(f"{negative} valor(es) negativo(s)")

