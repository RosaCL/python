import random
from time import sleep
print('Vou pensar em um número entre 0 e 5. Tente advinhar....')
n=int(input('Digite Em que número eu pensei?'))
print('Processando...')
sleep(2)
lista=[0,5]
escolhido=random.choice(lista)
if n==escolhido:
    print('Você acertou! Eu escolhi {} também!'.format(escolhido))
else:
    print('Você errou! Eu pensei no {} e não no {}!'.format(escolhido, n))

