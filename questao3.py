print('Digite o tamanho das retas que você deseja saber se formam um triângulo:')
r1 = float(input('reta 1:'))
r2 = float(input('reta 2:'))
r3 = float(input('reta 3:'))
g = r1 + r2
p = r1 - r2
if g > r3 > abs(p):
    print('Essas retas formam um triângulo.')
else:
    print('Essas retas não podem formar um triângulo.')