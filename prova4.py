#Escreva um programa que receba 3 números
#inteiros (A, B e N) e imprima todos os múltiplos de N no intervalo entre A e B. É
#interessante salientar que não necessariamente A<B, então você deve tratar isso
#também em seu código!

#Exemplo: Entrada: 1 10 2
#Saída: 2 4 6 8 10
a = 0
multiplos = 0
while (not a):
     a = int(input("Digite um valor inteiro para A"))
     if (a>0):
        a = 1
b = int(input("Digite um inteiro valor para b:"))
for n in range(b, a):
    if(n%a==0 and n%b==0):
       multiplos += n
print("Os multiplos dos números entre A e B são", multiplos)