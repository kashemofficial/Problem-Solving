a = list(input())
b = list(input())
vowels = ["a","e","i","o","u"]
a = [i in vowels for i in a]
b = [i in vowels for i in b]
if a==b:
      print("Yes")
else:
      print("No")
