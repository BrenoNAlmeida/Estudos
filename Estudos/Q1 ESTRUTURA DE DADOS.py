lista = [ 12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52 ]  
print(max(lista))
print(min(lista))
print("pares a seguir")
for c in lista:
    if c % 2 == 0:
        print(c)
print("=====fim=====")
print(lista.count(12))
media = 0
for i in lista:
    media += i
soma = 0
print(media/len(lista))
for m in lista:
    if m < 0:
        soma += m
print(soma)
