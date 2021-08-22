A,B,C = map(float,input().split())
pi = 3.14159
triangle = (C*A)/2
circle   = pi*pow(C,2)
trapezium= ((A+B)/2)*C
square   = pow(B,2)
rectangle= A*B
print("TRIANGULO: %.3f"%triangle)
print("CIRCULO: %.3f"%circle)
print("TRAPEZIO: %.3f"%trapezium)
print("QUADRADO: %.3f"%square)
print("RETANGULO: %.3f"%rectangle)

