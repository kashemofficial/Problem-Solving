age = int(input())
year = int(age/365)
month = int((age%365)/30)
days = int(age%365 % 30)

print("%i ano(s)"%year)
print("%i mes(es)"%month)
print("%i dia(s)"%days)

