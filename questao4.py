num = int(input("Fatorial de: ") )

resultado=1
count=1

while count <= num:
    resultado *= count
    count += 1

print('O fatorial do número digitado é:', resultado)