N = int(input())
print(N)
b = N/100
print("%i nota(s) de R$ 100,00"%b)
a = N%100
print("%i nota(s) de R$ 50,00"%(a/50))
a = a%50
print("%i nota(s) de R$ 20,00"%(a/20))
a = a%20
print("%i nota(s) de R$ 10,00"%(a/10))
a = a%10
print("%i nota(s) de R$ 5,00"%(a/5))
a = a%5
print("%i nota(s) de R$ 2,00"%(a/2))
a = a%2
print("%i nota(s) de R$ 1,00"%(a/1))
