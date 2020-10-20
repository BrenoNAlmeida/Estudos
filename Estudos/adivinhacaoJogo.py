numero_secreto = 42
rodada = 1
tentativas = 3
while (rodada <= tentativas ):
    print("rodada {} de {} tentativas".format(rodada, tentativas))
    numero = int(input("numero: "))
    acertou = numero == numero_secreto
    maior = numero > numero_secreto
    menor = numero < numero_secreto
    if(acertou):
        print("acertou")
        break
    elif(maior):
        print("o numero digitado é Maior que o numero secreto")
    elif(menor):
        print("o numero digitado é Menor que o numero secreto")
    rodada +=1
    
    
