#minha solução
import random
from time import sleep
print('Vou pensar em um número 0 a 10.Tente advinhar...')
n=int(input('Digite o número que pensei:'))
print('Processando...')
sleep(2)
lista=[0,10]
escolhido=random.choice(lista)
while n not in lista==n:
    n=int(input('Escolha outro número! Você não acertou!'))
    print('Você não acertou! Eu escolhi {} também.'(n))

#solução professor
from random import randint
computador=randint(0,10)
print('Vou pensar em um número 0 a 10.Tente advinhar...')
acertou=False
palpite=0
while not acertou:
    jogador=int(input('Qual é o seu palpite?'))
    palpite+=1
    if jogador==computador:
        acertou=True
    else:
        if jogador<computador:
            print('Mais...Tente mais uma vez.')
        elif jogador>computador:
            print('Menos...Tente mais uma vez.')
print('Você acertou com {} palpites.'.format(palpite))