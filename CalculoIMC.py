peso = input ("Qual é o seu peso? ")
altura = input ("Qual é a sua altura? ")

IMC = float(peso) / (float(altura) ** 2)

print ()

print ("Seu resultado do IMC é {:.1f}".format(IMC))

print ()

if IMC < 16.9:
    print ("Você está MUITO ABAIXO DO PESO, procure seu médico!")

if 16.9 <= IMC < 18.4:
    print ("Você está ABAIXO DO PESO, procure seu médico!")

if 18.4 <= IMC < 24.9:
    print ("Parabéns! Você está no PESO NORMAL")
    
if 24.9 <= IMC < 29.9:
    print ("Você está ACIMA DO PESO, procure seu médico!")
    
if 29.9 <= IMC < 34.9:
    print ("Você está com OBESIDADE GRAU I, procure seu médico!")
    
if 34.9 <= IMC < 40.0:
    print ("Você está com OBESIDADE GRAU II, procure seu médico!")

if IMC >= 40.0:
    print ("Você está com OBESIDADE GRAU III, procure seu médico!")
    
print()
    
if IMC <=18.4:
    print ("Quando se está abaixo do peso ideal deve-se aumentar o consumo de alimentos ricos em nutrientes para que o corpo tenha o necessário para se proteger de doenças.")
    
if IMC >= 25.0:
    print ( "Você não está dentro do peso ideal deve adequar a alimentação e fazer exercícios para conseguir atingir o peso mais indicado para sua altura e idade.")

print()

pesoidealminino= 18.5 * (float(altura) ** 2)
pesoidealmaximo= 24.9 * (float(altura) ** 2)
pesoideallista = int(pesoidealminino),int(pesoidealmaximo)

print ("Seu peso ideal é entre: " , pesoideallista)

