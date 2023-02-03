while True:
    try:
        num = float(input('Digite o número que deseja saber a raiz quadrada: '))
        if num < 0:
            raise ValueError('O número deve ser positivo')
    except ValueError:
        print(f'Valor inválido, digite um número positivo')
    else:
        print(f'A raiz quadrada de {num} é {num**(1/2):.3f}')
        break