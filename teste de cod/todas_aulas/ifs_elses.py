'''# True ou False deve ser escrito com a inicial maiuscula
sede = True 
banho = True 
fome = True

#and (e): significa que se TODAS as variaveis forem verdadeiras sera executado o comando
#(pode se dizer que se as duas forem verdadeiras o comando and é verdadeiro)
# se apenas uma for falsa o comando não é executado
# pode se passar diversos parametros a serem validados

if fome and sede and banho:
    print('vou comer um lanche, com suco')
else:
    print(' vou toma uma ducha antes')
    
    
sede = True
fome = False
banho = True

# or (ou): significa que alguma variavel deve ser verdadeira sera executado o comando
#(pode se dizer que se alguma for verdadeiras o comando Or é verdadeiro)
# se todas forem falsas o comando não é executado
# pode se passar diversos variaveis a serem validados

if fome or sede or banho:
    print('vou comer um lanche, com suco')
else:
    print(' vou toma uma ducha antes')
'''
'''sede = True
fome = True
    
# NOT ele inverte o valor( se é true vira false)
if sede and fome:
    print ("vou fazer um lache e beber algo")
elif sede and not fome:# aqui o codigo pensa que: sede é verdadeira e fome que estaria como falso mas foi invertida pelo NOT tambem é verdadeira, entao as duas sao verdadeiras e o comando é executado
    print(" vou apenas toma algo")
elif not sede and fome:#questão de logica
    print(' comer algo apenas')
else:
    print('vou jogar')
'''

num = 5
num1 = 32

if num == num1 :
    print('num é igual num1')


#   OPERADORES LOGICOS 
# OR == OU 
# AND == E
# NOT == NAO 

#   OPERADORES DE COMPARAÇÃO 
# == IGUAL 
# != DIFERENTE 
# > MAIOR
# < MENOR 
# >= MAIOR OU IGUAL
# <= MENOR OU IGUAL