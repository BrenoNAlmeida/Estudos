arq = dict()
op = 's'
lista = []
n = 1
while op != 'n':
    arq ['nome{}'.format(n)] = input()
    arq ['idade{}'.format(n)] = int(input())
    arq ['cidade{}'.format(n)] = input()
    lista.append(arq)
    op = input("adicionar outra pessoa ? [s/n]").lower()
    n +=1
for c in lista:
    print(c)
