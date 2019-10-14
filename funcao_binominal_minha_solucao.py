#função fatorial e um numero binominal que vai chamar 03X a função

x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))

if y == 1 or y == x:
  print('1')

if y > x:
  print('0')
    
else: 
    a = math.factorial(x)
    b = math.factorial(y)
    div = a // (b*(x-y))
    print ("Binomial(%d, %d) = %d" %(x, y, div))

    
    