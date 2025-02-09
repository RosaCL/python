Maior=0
Menor=0
for c in range (1,6):
    p=float(input('Qual o peso da {}ª pessoa Kg:'.format(c)))
    if c==1:
        Maior=p
        Menor=p
    else:
        if p>Maior:
            Maior=p
        if p<Menor:
            Menor=p
print ('O maior peso foi {} Kg e o menor peso foi {} Kg.'.format(Maior,Menor))