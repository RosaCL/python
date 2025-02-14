valor1=float(input("Digite um valor:")) 
valor2=float(input("Digite um valor:")) 
opcao=0
while opcao!=5:
    print('''
        [1] somar
        [2] multiplicar
        [3] maior
        [4] novos números
        [5] sair do programa 
        ''')
    opcao=int(input('Qual é a sua opção?'))
    if opcao==1:
        soma=valor1+valor2
        print('{} + {} = {}'.format(valor1,valor2,soma))
    elif opcao==2:
        mult=valor1*valor2
        print('{}x{}={}'.format(valor1,valor2,mult))
    elif opcao==3:
        if valor1>valor2:
            maior=valor1
        else:
            maior=valor2
        print('Entre {} e {} o maior é {}'.format(valor1,valor2,maior))
    elif opcao==4:
        print('Informe novos valores.')
        valor1=float(input("Digite um valor:")) 
        valor2=float(input("Digite um valor:")) 
    elif opcao==5:
        print('Finalizado!')
    else:
        print('Opção inválida! Tente novamente.')
print ("Fim do programa. Volte Sempre!")       

    
