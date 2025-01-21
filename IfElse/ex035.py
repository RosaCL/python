print('=='*20)
print("Analisador de triângulos")
print('=='*20)
r1=float(input("Digite o valor da 1º reta:"))
r2=float(input("Digite o valor da 2º reta:"))
r3=float(input("Digite o valor da 3º reta:"))
if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print("Os seguimentos acima podem formar um triângulo!")
else:
    print('Os seguimentos acima não formam um triângulo!')