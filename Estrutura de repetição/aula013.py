for c in range(1,7):# vai em ordem crescente
    print(c)
print('fim')

for c in range(7,0,-1): #vai em ordem decrescente
    print(c)
print('fim')

for c in range(0,7,2): #pula de 2 em 2
    print(c)
print('fim')

n=int(input('Digite um némero:')) #com começa do zero, para ir a até o número desejado tem que por +1
for c in range (0,n+1):
    print (c)
print("fim")

i=int(input('Inicio:'))
f=int(input('Fim:'))
p=int(input('Passo:'))
for c in range (i,f+1,p):
    print (c)
print('Acabou')

for c in range(0,3):
    n=int(input('Digite um valor:'))
print('Cest la vie')