def cont_caracteres(s):
    """funçao que conta os caracteres
        
        EX:
        >>> cont_caracteres('breno')
        b: 1
        r: 1
        e: 1
        n: 1
        o: 1
        >>> cont_caracteres('banana')
        a: 3
        n: 2
        b: 1
    """
    caracteres_ordenados = sorted(s)
    caracteres_antigos = caracteres_ordenados[0]
    cont = 1
    for caracter in caracteres_ordenados[1:]:
        if caracter == caracteres_antigos:
            cont +=1
        else:
            print(f'{caracteres_antigos}: {cont}')
            caracteres_antigos = caracter
            cont = 1 
        
    print(f'{caracteres_antigos}: {cont}')

if __name__ == "__main__":
    cont_caracteres('breno')
    print(" ")
    cont_caracteres('banana')
