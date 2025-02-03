from random import randint
from time import sleep
itens=('Pedra', 'Papel', 'Tesoura')
computador=randint(0,2)
print('''Suas opções:
        [0] Pedra
        [1] Papel
        [2] Tesoura''')
print('-'*20)
jogador=int(input('Qual é a sua jogada?'))
print('JO')
sleep(1)
print('Ken')
sleep(1)
print('PO!!!')
print('Computador escolheu {}.'.format(itens[computador]))
print('Jogador escolheu {}.'.format(itens[jogador]))
print('-'*20)
if computador==0: # Computador jogou pedra
    if jogador==0:
        print("Empate")
    elif jogador==1:
        print('Jogador vence!')
    elif jogador==2:
        print ('Computador vence!')
    else:
        print('Jogada Inválida!')
elif computador==1: # Computador jogou papel
    if jogador==0:
        print ('Computador vence!')
    elif jogador==1:
        print("Empate")
    elif jogador==2:
        print('Jogador vence!')
    else:
        print('Jogada Inválida!')
elif computador==2: #Computador jogou tesoura
    if jogador==0:
        print('Jogador vence!')
    elif jogador==1:
        print ('Computador vence!')
    elif jogador==2:
        print("Empate")
    else:
        print('Jogada Inválida!')