l1=float(input('Digite o valor do primeiro lado:'))
l2=float(input('Digite o valor do segundo lado:'))
l3=float(input('Digite o valor do terceiro lado:'))
print('=='*20)
print("Analisador de triângulos")
print('=='*20)
if l1<l2+l3 and l2<l1+l3 and l3<l1+l2:
    print('As retas formam um TRIÂNGULO')
    if l1==l2==l3:
        print ('EQUILÁTERO: todos os lados iguais')
    elif l1!=l2 !=l3 != l1:
        print ('ESCALENO: todos os lados diferentes')
    else:
        print('ISÓSCELES: dois lados iguais, um diferente')
else:
    print('Essas retas não formam um triângulo.')