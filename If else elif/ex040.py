n1=float(input('Digite a primeira nota:'))
n2=float(input('Digite a segunda nota:'))
media=(n1+n2)/2
if media>=7:
    print('Sua média foi {:.2f}.Aprovado!'.format(media))
elif media>=5 and media<7:
    print("Sua média foi {:.2f}.Você está em Recuperação!".format(media))
else:
    print('Sua média foi {:.2f}.Reprovado!'.format(media))