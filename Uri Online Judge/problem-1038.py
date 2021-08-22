x,y = map(int,input().split())
if (x == 1):
     y = y * 4.00
elif (x == 2):
    y = y * 4.50
elif (x == 3):
    y = y * 5.00
elif (x == 4):
    y = y * 2.00
elif (x == 5):
    y = y * 1.50
print("Total: R$ %.2f"%y)
