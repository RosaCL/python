t=float(input('Digite a temperatura em Celsius: '))
print('A temperatura {:.2F} ºC  em Fahrenheit é {:.2F} ºF'.format(t,((t*9)/5)+32))

tf=float(input('Digite a temperatura em Fahrenheit: '))
print('A temperatura {:.2f} ºF  em Celsius é {:.2F} ºC'.format(tf,(tf-32)*5/9))