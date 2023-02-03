carro_n = 0
carro_v = 0
contador = 0
continuar = 's'

while continuar == 's':
    velocidade = int(input('Digite a velocidade:'))
    ano = int(input('Digite o ano do carro:'))
    contador += 1
    if carro_v < velocidade: 
        carro_v = velocidade
        if ano > carro_n:
            carro_n = ano
            #contador =+ 1
    resposta = str(input("Você deseja continuar [s/n]"))
    if resposta == 's':
        print('continue o programa')
    else:
        #contador =+1
        continuar = resposta
print('O carro mais novo é:', carro_n)
print('O carro mais rápido é:', carro_v)
print('A quantidade de carros inserida foi:', contador)
                  