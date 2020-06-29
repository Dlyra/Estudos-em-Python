def fibonacci(i):
    if i <=2:
        print(f'Na posição: {i}\t A sequência Fibonaccci é: 1') 
    first = 1  #primeira posição
    second = 1  #segunda posição
    position = 3 
    while position <= i:
        result = first + second
        first = second
        second = result
        position = position + 1
    print(f'Na posição: {i}\t A sequência Fibonaccci é: {result}')    

