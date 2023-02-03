try:
    vetor = list()
    primeiroElemento = 0
    contMaiores = 0
    contMenores = 0
    igualElemento1 = 0
    for i in range(10):
        vetor.append(int(input('Digite um valor: ')))
    for i in vetor:
        if i == vetor[0]:
            primeiroElemento = i
        if i > primeiroElemento:
            contMaiores += 1
        if i < primeiroElemento:
            contMenores += 1
        if i == primeiroElemento:
            igualElemento1 += 1   
    print(f'Vetor: {vetor}')
    print(f'Primeiro elemento: {primeiroElemento}')
    print(f'Qtd de elementos maiores que o primeiro: {contMaiores}')
    print(f'Qtd de elementos menores que o primeiro: {contMenores}')
    print(f'Qtd de elementos iguais ao primeiro: {(igualElemento1)-1}')
except ValueError:
    print("ERRO! Tente novamente! Você digitou um número sem ser inteiro.")