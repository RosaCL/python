nome=str(input('Digite seu nome completo:')).strip().upper()
nc=nome.split()
print("Muito prazer em te conhecer! {}".format(nome))
print('Seu primeiro nome é {}'.format(nc[0]))
print('Seu último nome é {}'.format(nc[len(nc)-1]))
