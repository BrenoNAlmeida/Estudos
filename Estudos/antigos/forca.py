def jogar():
    import random
    acertou = False
    enforcou = False
    palavra_secreta = "banana"
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()
    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper().strip()
    letras_acertadas = ['_' for letras in palavra_secreta]
    erros = 0
    print(letras_acertadas)
    while(not acertou and not enforcou ):
        chute = input("Qual letra ? ")
        chute = chute.upper()
        posicao = 0
        for letra in palavra_secreta:
            if chute == letra:
                letras_acertadas[posicao] = letra
            posicao += 1
        else:
           erros +=1
        print(letras_acertadas)
        acertou = "_" not in letras_acertadas
        enforcou = erros == 6
    if(acertou):
        print("voce ganhou")
    elif (enforcou):
        print("voce perdeu")


