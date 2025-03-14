
# EX 4
dolar = [4.95, 4.97, 5.01, 5.19, 5.24, 5.59, 5.65, 5.61, 5.42, 5.78, 5.97, 6.17]
atual = 0

def cofrinho(salario, mes = 0): #mes = 0 é o valor padrão para o mês, que é o primeiro mês de   
    salario
    
    poupança = salario
    
    cotacao_hoje = dolar[mes % 12]
    renda =  poupança %  cotacao_hoje
    
    poupança += renda + (renda * 0.05)
    atual = poupança * cotacao_hoje
    if atual == 1000000:
        return print("congratulations")
    
    if atual >=100000:
        print("100k")
    
    mes +=1
    return cofrinho(salario, mes) # tipo while, mas recursivo

print(cofrinho(500))