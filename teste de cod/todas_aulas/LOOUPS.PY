'''i = int(input(" qual a sua idade: "))
if i < 0:
    print('coloque uma idade valida')
else:
    while i <18: #while : ele faz determinado comando ate que o valor seja verdadeiro. Nesse caso, ate i for igual a 18 ele nao vai parar de rodar o codigo

        print(i)
        i += 1

print("vc atingiu a maioridade")

print('terminou')
print(i)

irmaos = ["giovana ", "Gabriela", "isabela", "diogo", "kaique"]

for item in irmaos:
    print(item)


for index in range(len(irmaos)):
    print(irmaos[index], index)
   
 


#for bola in range(5,100,5):# 3 parametros, 1 inico, 2 ate onde vai, 3 step(pulo) 
 #   print(bola)'''

matrix_numeros = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0],
]

for linha in matrix_numeros:
    for coluna in linha :
        print(coluna)
        for boa in coluna:
            print(boa)