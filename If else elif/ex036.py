valorCasa=float(input('Valor da casa: R$'))
salario=float(input('Sálario do comprador: R$'))
anos=int(input('Quantos anos de financiamento?'))
prestação=valorCasa/(anos*12)
minimo=salario*30/100
print('Para pagar uma casa de R${:.2f} em {} anos.'.format(valorCasa,anos), end='')
print('A prestação será de R${:.2f}'.format(prestação))
if prestação<=minimo:
    print('Empréstimo CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')