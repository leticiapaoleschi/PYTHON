#Uma grande empresa de tecnologia está realizando o
#cadastro das três profissões que possuem vaga em aberto, sendo elas:
#desenvolvedor python, cientista de dados e analista de requisitos. Para cada uma
#dessas profissões deverá ser cadastrado o salário médio, tempo mínimo de
#experiência e o valor da hora de trabalho. Na sequência, utilizando matrizes,
#desenvolva um programa que faça esse cadastro e, na sequência:
#a) Mostre a matriz na tela com os valores em formato de tabela;
#b) A média salarial das três profissões;
#c) A soma dos valores da diagonal principal (valores em preto);
matriz = [[], [], []]
soma = 0
for l in range(3):
    for c in range(3):
        matriz[l].append(int(input('[{}][{}]Digite o valor do seu salário, seu tempo minimo de experiência e o valor da sua hora: '.format(l,c))))
for l in range(3):
    for c in range(3):
        print(f"{matriz[l][c]:^3}", end="")
    print()    
soma = matriz[0][0] + matriz[1][1] + matriz[2][2]
media = (matriz[0][0] + matriz[1][0] + matriz[2][0])/3
print(matriz)
print(soma)
print("A média dos salários é:", media)

