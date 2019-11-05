
meuCartão = int(input("Digite o número do seu cartão de crédito: "))

cartãolido = 1 
encontreiMeuCartãonalista = False

while cartãolido != 0 and not encontreiMeuCartãonalista:
    cartãolido = int(input("Digite o número do próximo cartão de crédito: "))
    if cartãolido == meuCartão : 
        encontreiMeuCartãonalista = True

if encontreiMeuCartãonalista:
    print ("EBA!!! Meu cartão está lá!")
else: 
     print ("Xi, meu cartão não está lá...")
        