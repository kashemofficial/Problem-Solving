p1_code,p1_unit,p1_pro = map(float,input().split())
p2_code,p2_unit,p3_pro= map(float,input().split())
total=((p1_unit*p1_pro)+(p2_unit*p3_pro))
print("VALOR A PAGAR: R$ %.2f"%total)
