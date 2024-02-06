# #set- lista desordenada que nao aceitar valores iguais
# frutas = {" maca ", 'laranja ', 'terra'}
# #nao ha indices pq nao ha sequecia correta no set

# frutas.add("casca")# adiciona um valor

# frutas.pop()#elimina o ultimo valor

# frutas.remove(" maca ")# exlui valor especifico 

# frutas.add(23)# aceita qualquer valor

# print(frutas)

#dict - dicionario tem uma chave que serve como nome e recebe um valor
#como um dicionario mesmo, cada palavra tem seu significado

meses = {#nao aceita valore duplicados
    "jan" : "janeirao",
    "fev" : "carnaval",
    "mar" : "meus irmaos",
    "abril" : "meu amor",
    "jun" : " festa junina",
    "jul" : "festa julhina",
    "maio" : "n sei nao",
    "sep" : " mes 9 com nome de sete",

}
print(meses.get("abril", "treta"))#chaves erradas retornam o outro valor