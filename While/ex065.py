resp="S"
media=quant=soma=maior=menor=0
while resp in 'Ss':
    n=int(input("Digite um número:"))
    soma+=n
    quant+=1
    if quant==1:
        maior=menor=n
    else:
        if n>maior:
            maior=n
        if n<menor:
            menor=n
    resp=str(input('Quer continuar [S/N]:')).upper().strip()[0]
media=soma/quant
print("Você digitou {} número e a média foi {}.".format(quant,media))
print('O maior valor foi {} e o menor foi {}.'.format(maior,menor))