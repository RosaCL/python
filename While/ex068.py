from random import randint
v=0
print("#"*30)
print('Vamos jogar par ou impar')
print("#"*30)
while True:
    j=int(input("Digite um valor:"))
    pc=randint(0,11)
    total=j+pc
    tipo=' '
    while tipo not in 'PpIi':
        tipo=str(input('Par ou Impar:')).strip().upper()[0]
    print(' Você jogou {} e o computador {}. Total de {}.'.format(j,pc,total))
    if tipo=='P':
        if total%2==0:
            print ('Você venceu!')
            v+=1
        else:
            print('Você perdeu!')
            break
        
    elif tipo=='I':
        if total%2==1:
            print ('Você venceu!')
            v+=1
        else:
            print('Você perdeu!')
            break
    print ('Vamos jogar novamente!')
print('Game Over! Você venceu {} vezes.'.format(v))