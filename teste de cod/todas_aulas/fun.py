'''Coleções de  codigo ou logica em uma coluna só. 
encapsular todo o trabalho e reutilizar o comando

def big_mac():# tudo baseado em identação
    print(' sanduiche big mac')


big_mac()
def fazer_batata(tamanho):
    print('batata {}'.format(tamanho))


def coca(tipo, tamanho) :
    print('{} {}'.format(tipo, tamanho))

def fazer_bk(nome):
    print (f'sanduba {nome}')


fazer_bk("gui")
fazer_batata("grande")
coca("coca " ,"med")'''

def pedido(lanche=0 , bebida=0, batata=0):
    lanche = str(input("qual lanche deseja "))
    bebida = str(input("qual bebida deseja "))
    batata = str(input('Qual batata deseja '))
    print('voce pediu um lanche {}, uma {}, e uma batata {}'.format(lanche, bebida, batata))



pedido()

       