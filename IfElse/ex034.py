s=float(input('Qual é o sálario do funcionário?R$'))
if s<=1250:
    print("O funcinário com o R${} receberá 15% de aumento, ficando com R${:.2f}".format(s, (((15/100)*s)+s)))
else:
    print("O funcinário com o R${} receberá 10% de aumento, ficando com R${:.2f}".format(s, ((10/100)*s)+s))