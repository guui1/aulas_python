def jogo():

    try:
        while exit:
            

            def par ():
                num1 =int(input('Digite um numero QUALQUER: '))

                num2 = num1 % 2
                if num2 == 1:
                    print(f'O numero {num1}, é um numero INPAR')
                else:
                    print(f'O numero {num1}, é um numero PAR')

            par()
    except ValueError:
        print('apenas numeros amigo')

jogo()