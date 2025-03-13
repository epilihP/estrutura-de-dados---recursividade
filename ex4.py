
# EX 4

def poupança():
    poupança = 0
    while poupança != 1000000:
        
        dolar = [4.9526, 4.9716, 5.0153, 5.1934, 5.2443, 5.5925, 5.6500, 5.6103, 5.4482, 5.7867, 5.9730, 6.1778] # meses do dolar taca na recusiva 
        for i in range (dolar):
            renda = (i[0] % poupança())
            poupança +=renda + (renda*0,05)
            atual = poupança * i[0]
            if atual >= 1000000:
                return print("U have 1bi")
            else:
                continue
        return print("U dont can né?!")