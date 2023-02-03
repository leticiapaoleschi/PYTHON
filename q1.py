
nomes=[]
idades=[]
sobrenomes = []
p=int(input("Informe a quantidade de pessoas a serem cadastradas:"))

for i in range(p):
    nome=str(input("Informe o nome:"))
    nomes.append(nome)
    sobrenome=str(input("Informe o sobrenome:"))
    sobrenomes.append(sobrenome)
    idade=int(input("Informe a idade:"))
    idades.append(idade)
    

file=open("arquivo.txt","w")
file.write(f"Existem {p} pessoas cadastradas\n")
for j in range(p):
    file.write(nomes[j-1])
    file.write(sobrenomes[j-1])
    file.write(f":{idades[j-1]}\n")
print(file)
file.close()
    
