d=float(input('Qual é a distância da sua viagem?'))
print('Você está prestes a começar uma viagem de {} Km.'.format(d))
if d<=200:
    p=d*0.50
    print('E o preço da sua passagem será de  R$ {}'.format(p))
else:
    p=d*0.45
    print('E o preço da sua passagem será de  R$ {}'.format(p))
    