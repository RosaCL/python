n=float(input('Digite um número com casa decimais: '))
print('O número {} convertido para número inteiro é {}'.format(n, int (n)))


# usando biblioteca
from math import trunc
n=float(input('Digite um número com casa decimais: '))
print('O número {} convertido para número inteiro é {}'.format(n, trunc(n)))