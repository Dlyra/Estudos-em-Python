#função fatorial e um numero binominal que vai chamar 03X a função

import math

x = int(input("Digite o número de termos: "))
y = int(input("Digite o número da classe: "))

if y == 1 or y == x:
  print(1)

if y > x:
  print(0)
    
else: 
    a = math.factorial(x)
    b = math.factorial(y)
    div = a // (b*(x-y))
    print ("Número Binominal é ", div)
    
  def coef_binominal (n,k):
    return  //(k*(n-k))