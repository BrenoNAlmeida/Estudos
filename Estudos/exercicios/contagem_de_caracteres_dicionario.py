def cont_caracteres(s):
    """funçao que conta os caracteres

        EX:
        >>> cont_caracteres('breno')
        {'b': 1,'r': 1,'e': 1,'n': 1',o': 1}
        >>> cont_caracteres('banana')
        {'a': 3,'n': 2,'b':1}
        
    """
    resultado = {}
    for caracter in s:
        """esse for percorre os caracters em S, conta os caracteres 
        e adiciona no dicionario 'resultado'"""
        resultado[caracter]= resultado.get(caracter, 0) + 1
    return resultado

if __name__ == "__main__":
    print(cont_caracteres('breno'))
    print(" ")
    print(cont_caracteres('banana'))