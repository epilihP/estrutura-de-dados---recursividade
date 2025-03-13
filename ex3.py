
#  EX 3 INVERSÃO DE STRING

def inversão(texto):
    if len(texto) == 0:
        return texto
    return texto[-1] + inversão(texto[:-1])
inversão()