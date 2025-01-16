#condição simples
nome=str(input("Qual é o seu nome?"))
if nome=='Rosa': # apenas se a condição for atendida
    print('Você é uma gostosa inteligente!')
print('Bom dia, {}!'.format(nome)) #sempre vai acontecer

#condição composta
nome=str(input("Qual é o seu nome?"))
if nome=='Rosa': # apenas se a condição for atendida
    print('Você é uma gostosa inteligente!')
else:
    print('Você é legal!')
print('Bom dia, {}!'.format(nome)) #sempre vai acontecer


tempo=int(input('Quanto tempo tem seu carro?'))
if tempo<=3:
    print('Carro novo')
else:
    print('Carro velho')

n1=float(input('Digite a primeira nota:'))
n2=float(input('Digite a segunda nota:'))
m=(n1+n2)/2
print('Sua média foi {}'.format(m))
if m>=7:
    print('Parabéns!!!Você passou!')
else:
    print('Você foi Reprovado!!!Estude mais!')