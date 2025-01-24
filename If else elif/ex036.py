vc=float(input('Valor da casa: R$'))
s=float(input('Sálario do comprador: R$'))
a=int(input('Quantos anos de financiamento?'))
p=vc/(a*12)
minimo=s*30/100
print('Para pagar uma casa de R${:.2f} em {} anos.'.format(vc,a), end='')
print('A prestação será de R${:.2f}'.format(p))
if p<=minimo:
    print('Empréstimo CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')