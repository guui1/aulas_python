familia = ['gui', 'bela', 'digo', 'gordo', 'giba']
#            0       1      2        3
#            -4        -3       -2         -1


#print(familia[-1])
#print(familia[-4])
#print(familia)
#familia[3] = "roger"
print(familia)

familia.extend(["pai", "mae"])
print(familia)
familia.append("dog")
print(familia)
familia.insert(2,'duda')
print(familia)
familia.pop(2)
familia.remove('giba')
print(familia)



idade_familia=[22,52,12,30]
print(idade_familia)
idade_familia.sort()
print(idade_familia)
familia.sort()
print(familia)
familia.reverse()
print(familia)
familia_2 = familia # um espelho da lista em uma variavel
print(familia_2)

familia_3 = familia.copy() #copia a lista da forma que ela esta neste ponto do codigo
print(familia_3)
familia.pop()
print(familia)
print(familia_2)
print(familia_3)