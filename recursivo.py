# EX 1 FATORIAL
def fatorial_recursivo(fatorial):

    if fatorial == 0 or fatorial ==1:
        return 1

    return fatorial  * fatorial_recursivo(fatorial -1)
    

# EX 2 SOMA

def soma_list_recursivasso(lista):
    if not lista == list:
        return 0
    
    return 0 + soma_list_recursivasso[1:]

#  EX 3 INVERSÃO DE STRING

def inversão(texto):
    if len(texto) == 0:
        return texto
    return texto[-1] + inversão(texto[:-1])


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
 

 # EX 5 btc

def bitcoin(bitcoins_na_conta = 0, mes = 0):
    valor_bitcoin = 664484
    cotacao_bitcoin = [209410, 212335, 306600, 359693, 316517, 355299, 352500, 368540, 333842, 345411, 409131, 580819]
    investimento_reais = 250
    rendimento = 0.0005
    meta100k = 100000
    meta1m = 1000000
    metabitcoin = valor_bitcoin

    cotacao_atual = cotacao_bitcoin[mes % 12]
    investimento_bitcoin = investimento_reais/cotacao_atual
    bitcoins_na_conta *= (1+rendimento)

    bitcoins_na_conta += investimento_bitcoin
    mes += 1
    
    reais_na_conta = bitcoins_na_conta * cotacao_atual

    if reais_na_conta >= meta100k:
        print(f'Meta de R${meta100k} atingida em {mes} meses')
        return mes, mes*investimento_reais, reais_na_conta
    
    if reais_na_conta >= meta1m:
        print(f'Meta de R${meta1m} atingida em {mes} meses')
        return mes, mes*investimento_reais, reais_na_conta
    
    if reais_na_conta >= metabitcoin:
        print(f'Meta de 1 bitcoin atingida em {mes} meses') 

    return bitcoin(bitcoins_na_conta, mes)

meses, valor_investido_brl, saldo_final_brl = bitcoin()
print(f"- Meses: {meses}")
print(f"- Valor investido (BRL): R$ {valor_investido_brl:.2f}")
print(f"- Saldo final (BRL): R$ {saldo_final_brl:.2f}")




# EX 6  açõexxxx
def ações():
    saldo = 0
    meses = 0
    investido = 0
    investimento_mensal = 80
    
    div_marfrig = 0.2983
    div_petrobras = 0.1349
    div_itausa = 0.10
    div_medio = (div_petrobras + div_marfrig + div_itausa) / 3
    div_mensal = div_medio / 12
    
    marco_100k = None
    
    while saldo < 1000000:
        saldo += investimento_mensal
        investido += investimento_mensal
        dividendos = saldo * div_mensal
        saldo += dividendos
        meses += 1
        
        if saldo >= 100000 and marco_100k is None:
            marco_100k = (meses, investido, dividendos)
    
    anos = meses // 12
    meses_restantes = meses % 12
    
    print("Tempo gasto até R$100 mil:", marco_100k[0] // 12, "anos e", marco_100k[0] % 12, "meses")
    print("Investido até R$100 mil:", "R$", round(marco_100k[1], 2))
    print("Tempo até R$1 milhão:", anos, "anos e", meses_restantes, "meses")
    print("Saldo final:", "R$", round(saldo, 2))
    
    
