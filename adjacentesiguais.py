
adjacentesiguais = False
x = int(input("Digite o número que deseja verificar: "))

r = x % 10
i = x // 10

ultimor = r

while i > 0: 
    r = (i % 10)
    i = i // 10 
    if (ultimor == r):
        adjacentesiguais = True
        break
    ultimor = r
    
print()

if adjacentesiguais:
    print ("Sua sequência tem números adjacentes iguais")
else:
    print ("Sua sequência não tem números adjacentes iguais")
    
    


