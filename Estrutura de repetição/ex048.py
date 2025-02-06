soma=0
c=0
for n in range (1,501,2):
    if n%3==0:
        c=c+1
        soma=soma+n
print('A soma entre todos os {} números que são múltiplos de três e que se encontram no intervalo de 1 até 500 é {}'.format(c,soma))