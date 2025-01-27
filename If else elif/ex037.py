n=int(input('Digite um número inteiro:'))
print('''Escolha uma das bases para conversão: 
    [1] converter para Binário 
    [2] converter para Octal 
    [3] converter para Hexadecimal''')
opcao=int(input('Sua opção:'))
if opcao==1:
    print('{} em binário é {}.'.format(n,bin(n)[2:]))
elif opcao==2:
    print('{} em octal é {}.'.format(n,oct(n)[2:])) 
elif opcao==3:
    print('{} em hexadecimal é {}.'. format(n,hex(n)[2:]))
else:
    print('Opção inválida. Tente novamente.')