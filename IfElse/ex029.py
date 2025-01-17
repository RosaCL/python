v=float(input('Qual é a velocidade atual do carro? '))
multa=(v-80)*7
if v>80:
    print('Você foi multado!Você excedeu o limite permitido de 80Km/h. Você pagara R$ {}'.format(multa))
else: 
    print('Boa viagem!!!Dirija com segurança.')