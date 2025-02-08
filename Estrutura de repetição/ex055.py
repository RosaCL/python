Maior=0
Menor=0
for c in range (1,6):
    p=float(input('Qual o peso da {}ª pessoa Kg:'.format(c)))
    if c==1:
        Maior=c
        Menor=c
    else:
        if p>Maior:
            Maior=p
        if p<Menor:
            Menor=p
print ('O maior peso foi {} e o menor peso foi {}.'.format(Maior,Menor))