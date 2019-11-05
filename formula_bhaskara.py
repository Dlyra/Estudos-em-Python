import math

coeficienteA = float(input("Insira o valor do coeficiente a: "))
coeficienteB = float(input("Insira o valor do coeficiente b: "))
coeficienteC = float(input("Insira o valor do coeficiente c: "))

delta = (coeficienteB ** 2)- (4 * coeficienteA * coeficienteC)

print()

if delta < 0:
        print ("A equação não possui resultados reais")
else:
    x1 = (- coeficienteB + math.sqrt (delta)) / (2 * coeficienteA)
    x2 = (- coeficienteB - math.sqrt (delta)) / (2 * coeficienteA)
    print()
    if delta == 0:
        print ("A equação possui apenas um resultado real: {:.2f}". format(x1))
    else:
        print ("A equação possui dois resultados distintos reais, são eles: {:.2f}". format(x1),"e {:.2f}" . format(x2))




    
