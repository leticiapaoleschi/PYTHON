#Um número é
#considerado triangular se ele é produto de três números naturais consecutivos.
#Por exemplo: 120 é triangular, pois 4*5*6 = 120. O número 2730 é triangular, pois
#13*14*15 = 2730. Após o usuário digitar um número natural (inteiro não-
#negativo), verifique se ele é triangular ou não.
n = int(input("Digite um número que você deseja saber se é triangular:"))
cont = 1
for n in range(n):
 if (n>cont):
    if (n-1)*(n-2)*(n-3) == n:
         print("Este número é triangular", n)
 else:
    print("Este número não é triangular")  
    
          