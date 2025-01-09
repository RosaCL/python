from math import hypot
co=float(input("Digite o cateto oposto:"))
ca=float(input('Digite o cateto adjacente:'))
h=hypot(co,ca)
print('O cate to oposto é {} e o cateto adjacente é {}, sua hipotenusa é {:.2f}'.format(co,ca,h ))

# importando a biblioteca toda
import math
co=float(input("Digite o cateto oposto:"))
ca=float(input('Digite o cateto adjacente:'))
h=math.hypot(co,ca)
print('O cate to oposto é {} e o cateto adjacente é {}, sua hipotenusa é {:.2f}'.format(co,ca,h ))


#Fazendo o cacluclo 
co=float(input("Digite o cateto oposto:"))
ca=float(input('Digite o cateto adjacente:'))
h=(co**2+ca**2)**(1/2 )
print('O cate to oposto é {} e o cateto adjacente é {}, sua hipotenusa é {:.2f}'.format(co,ca,h ))
