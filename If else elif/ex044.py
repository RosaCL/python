print('{:=^40}' .format ('DINASTIA ROSA'))
v=float(input("O produto vale: R$"))
print('''Qual a forma de pagamento?
        [1] à vista dinheiro/ cheque
        [2] à vista cartão
        [3] 2x no cartão
        [4] 3 x ou mais no cartão
        ''')
OPÇAO= int(input('Qual é a opção de pagamento?'))
if OPÇAO==1:
    total= v-(v*10/100)
    print("Se você pagar em dinheiro ou cheque receberá 10% de desconto, de R${}, ficará R$ {}.".format(v,total))
elif OPÇAO==2:
    total=v-(v*5/100)
    print("Se você pagar em cartão a vista receberá 5% de desconto, de R${}, ficará R$ {}.".format(v,total))
elif OPÇAO==3:
    total=v/2
    print("Se você pagar em 2x no cartão a  compra ficará R${}, com uma parcela de {}.".format(v, total))
elif OPÇAO==4:
    total=v+(v*20/100)
    totalparc=int(input('Quantas parcelas?'))
    parcela=total/totalparc
    print("Se você pagar em {}x no cartão a  compra de R$ {}, com o juros ficará R${}, pagando uma parcela de R${:.2f} .".format(totalparc, v, total, parcela))
else:
    print("Opção inválida de pagamento. Tente novamente!")
    
    