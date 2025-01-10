import math
n=int(input('Digite um número:'))
raiz=math.sqrt(n)
print('A raiz de {} é igual a {:.2f}.'.format(n,raiz))
print('A raiz de {} é igual a {}.'.format(n,math.ceil(raiz))) #arredondado para cima
print('A raiz de {} é igual a {}.'.format(n,math.floor(raiz))) #arredondado para baixo