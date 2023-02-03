nomes = []
entrada = input('Digite o nome para inserir na lista ou "s" para sair: ')
while entrada != 's':
    if entrada != '':
        nomes.append(entrada)

    entrada = input('Digite o nome para inserir na lista ou "s" para sair: ')
nomes.sort()
arquivo = open('nomes.txt', 'w')
for nome in nomes:
    arquivo.write(nome + '\n')
arquivo.close()



    