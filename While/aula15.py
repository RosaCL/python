# looping infinito
c=1
while True:
    print(c,'...',end=' ')
    c+=1
print('acabou')

#interropendo loop utilizando flag
n=0
while n!=999:
    n=int(input('Digite um número:'))
    
n=s=0
while True:
    n=int(input('Digite um número:'))
    if n==999:
        break
    s+=n
print('A soma vale {}.'.format(s))
print(f'A soma vale {s}.') #f string nova forma de format