arquivo = open("ips_avaliar.txt", "r")
num = arquivo.read()
endereco = num.split('\n')
print(num)
print(endereco)
resposta = ''
for Endereco in endereco:
    ips = Endereco.split('.')
    for dividideIp in ips:
        converteIP = int(dividideIp)
        if converteIP > 224:
            resposta = 'endereço inválido'
        else:
            resposta = 'endereço válido'
    print(f'esse {Endereco} possui {resposta}')
    