# código com for 
frase=str(input('Digite uma frase:')).strip().upper()
palavras=frase.split()
junto=''.join(palavras)
inverso=''
for letra in range(len(junto)-1, -1,-1):
    inverso+=junto[letra]
if inverso==junto:
    print('Temos um palíndromo!')
else:
    print('NÃO temos um palíndromo!')
    
# código sem for  
frase=str(input('Digite uma frase:')).strip().upper()
palavras=frase.split()
junto=''.join(palavras)
inverso=''
inverso=junto[::-1]
if inverso==junto:
    print('Temos um palíndromo!')
else:
    print('NÃO temos um palíndromo!')
