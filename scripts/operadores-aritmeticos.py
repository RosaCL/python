# 5+2==7 soma
# 5-2==3 subtração
# 5*2==10 multiplicação
# 5/2==2.5 divisão
# 5**2==25 exponenciação
# 5//2==2 divisão inteira
# 5%2==1 resto de divisão
print(int(5+2))
print(int(5-2))
print(int(5*2))
print(int(5/2))
print(int(5**2))
print(int(5//2))
print(int(5%2))

# nome=input('Qual é o seu nome?')
# print('Prazer em te conhecer {:=^20}!' .format(nome))
# {:>20} mais de 20 espaços
# {:^20} mais de 20 espaços centralizado
# {:=^20} mais de 20 espaços centralizado entre o sinal de igualdade
# {:.3f} limita o numero de casa decimal

n1=int(input("Digite um valor:"))
n2=int(input('Digite outro valor:'))
s=n1+n2
sub=n1-n2
mult=n1*n2
div=n1/n2
exp=n1**n2
print('A soma vale {}, a subtração vale {}, a multiplicação vale {}, a divisão vale {:.3f} e a exponeciação vale {} '.format(s, sub, mult, div, exp))