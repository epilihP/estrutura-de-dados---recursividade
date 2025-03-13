# EX 1 FATORIAL
def fatorial_recursivo(fatorial):

    if fatorial == 0 or fatorial ==1:
        return 1

    return fatorial  * fatorial_recursivo(fatorial -1)
fatorial_recursivo()