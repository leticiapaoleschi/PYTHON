soma = 0
soma_cap = 0
for i in range(5):
    quantidade_caixa = int(input('Digite a quantidade de caixas que você deseja doar: '))
    soma = soma + quantidade_caixa
    numero_capsulas = int(input('Digite se a caixa vai ser de 10 ou 16 cápsulas:'))
    cap = quantidade_caixa * numero_capsulas
    soma_cap = soma_cap + cap

print('A quantidade de caixas doadas foram {}'.format(soma))
print('A quantidade de cápsulas doadas foi de {}'.format(soma_cap))
print('A quantidade de xicáras que cada professor vai poder consumir é de {}'.format(soma_cap/5))