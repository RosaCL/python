from datetime import date
atual=date.today().year
totalmaior=0
totalmenor=0
for c in range (1,8):
    nasc=int(input( 'Em que ano a {}ª pessoa nasceu?'.format(c) ))
    idade=atual-nasc
    if idade>=18:
        totalmaior+=1
    else:
        totalmenor+=1
print('Ao todo tivemos {} pessoas maiores de idade e {} pessoas menores de idade.'.format(totalmaior,totalmenor))
