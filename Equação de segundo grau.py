import math

A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))

print ()
    
Delta =  B**2 - 4 * A * C


if Delta < 0:

    print ("esta equação não possui raízes reais")


if Delta == 0:

    X1 = -B / (2 * A)

    print ("a raiz desta equação é",X1)

if Delta > 0:

    X1 = (-B + math.sqrt(Delta)) / (2 * A)

    X2 = (-B - math.sqrt(Delta)) / (2 * A)

    X1 > X2
    
    print("as raízes da equação são",X2,"e",X1
          )
    







    
    
