try: #tente executar o codigo abaixo, se der erro, o valor for invalido ou quebrar, ele vai passar para frente e rodar o codigo seguinte

    numero = int(input("digite um numero: "))

    print(numero)
 
    numero/2
except ZeroDivisionError:#caso o valor da varivel numero seja correto, esse comando sera executado com base no calculo acima
    print("divisão por zero nao é possivel")#ou caso de erro, ele passara para o de baixo
except ValueError:
    print("digite um valor valido")
except: #codigo a ser seguido se a "try quebrar"
    print('erro inesperado.')
#caso um banco de dados enorme tiver um valor quebrado ele nao vai quebrar inteiro.
finally:#idependente de qual except ocorrer esse codigo sera executado.
    print('Volte sempre ')