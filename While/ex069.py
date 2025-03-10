tot18=totH=totM20=0
print( "="*30)
print("Analise de dados")
print ("="*30)
while True:
    idade=int(input ("Idade:"))
    sexo=' '
    while sexo not in 'MF':
        sexo=str(input("Sexo: [M/F]")).strip().upper()[0]
    if idade>=18:
        tot18+=1
    if sexo=='M':
        totH+=1
    if sexo=='F' and idade<20:
        totM20+=1
        
    resp=' '
    while resp not in 'SN':
        resp=str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp=='N':
        break
print("Total de pessoas que tem mais de 18 anos: {}.".format(tot18))
print("Total de homens que foram cadastrados: {}". format(totH))
print('Total de mulheres que tem menos de 20 anos cadastrados: {}.'.format(totM20))