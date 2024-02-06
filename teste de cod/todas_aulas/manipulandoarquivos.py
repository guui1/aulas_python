#open("caminho" , ("r"))

# r - leitura
# a - incrementar adiciona novos valores
# w - escrita apaga os valores antigos
# x - criar arquivo
# r+ - leitura + escrita
arquivo = open ("teste2.txt","a") #"teste2.txt"criou um novo arquivo

print(arquivo.readable())#true or false para saber se o arquivo pode ser lido, há outro cmds como whiretable, para saber se o arquivo pode ser escrito
#depende de como este arquivo esta abre, nesse caso opne("r") leitura
print(arquivo.read())
print(arquivo.readline())#ler a primeira linha
print(arquivo.readline())# lê a segunda e etc
# print(arquivo.readline())
# print(arquivo.readline())
# print(arquivo.read())# lê o resto do arquivo todo,
#lista = arquivo.readlines()
#print(lista[1])

#arquivo.write("SQL")#adiciona um novo valor a lista, mas deve ser mudado o open para a
#arquivo.write("SQL\n")
#deve salvar o arquivo 

#arquivo.close() #sempre fechar o arquivo dps de usar.

#import os 
# if os.path.exists("teste2.txt"): #confere se o arquivo existe
#     os.remove("teste2.txt")# apagou o arquivo todo, para isso o arquivo deve ser fechado antes.
# else:     print(" arquivo nao existe")

#os.rmdir("novapasta")# apenas se a pasta estiver vazia