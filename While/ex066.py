s=c=0
while True:
    n=int(input("Digite um valor inteiro [999 para parar]:"))
    if n==999:
        break
    c+=1
    s+=n
print ("Você digitou {} valores, sua soma  foi {}.".format(c,s))