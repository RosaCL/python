total=totmil=menor=cont=0
barato=''
while True:
    produto=str(input('Nome do produto: '))
    preco=float(input('Preço: R$'))
    cont+=1
    total+=preco
    if preco>1000:
        totmil+=1
    if cont==1 or preco<menor:
        menor=preco  
        barato=produto
    resp=' '
    while resp not in 'SN':
        resp=str(input ('Quer contninuar? [S/N] ')).strip().upper()[0]    
    if resp=='N':
        break
print ('Fim do programa')
print('O total da compra foi R$ {:.2f}'.format(total))
print('Temos {} produtos custando mais de R$ 1.000,00'.format(totmil))
print(f'O produto mais barato foi  o {barato} custa R${menor:.2f}')