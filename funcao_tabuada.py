def tabuada ():
    for i in range(1,11):
        print(f'Tabuada de {i}')
        for j in range(1,11):
            result = i * j
            #print('{} x {} = {}'.format(i, j, result))  #interpolação de string
            print(f'{i} x {j} = {result}')  #interpolação de string
        print('\n')



