somaidade=0
media=0
maioridadeHomem=0
nomeVelho=''
totmulher20=0
for c in range (1,5):
    print('.......{}ª PESSOA.......'.format(c))
    nome=str(input('Nome:'))
    idade=int(input('Idade:'))
    sexo=str(input('Sexo (F/M):'))
    somaidade+=idade
    if c==1 and sexo in 'Mm':
        maioridadeHomem=idade
        nomeVelho=nome
    if sexo in 'Mm' and idade>maioridadeHomem:
        maioridadeHomem=idade
        nomeVelho=nome
    if sexo in 'Ff' and idade<20:
        totmulher20+=1
media=somaidade/4
print('A média de idade do grupo é de {} anos.'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadeHomem,nomeVelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher20))