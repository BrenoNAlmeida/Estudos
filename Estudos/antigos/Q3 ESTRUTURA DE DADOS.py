notas = []
for c in range (0,4):
    n = float(input("nota :"))
    notas.append(n)
print(notas)
media = 0
for i in notas:
    media += i
print(media/4)
