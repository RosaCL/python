sexo=str(input('Informe seu sexo (F/M):')).upper()[0].strip()
while sexo not in 'MmFf':
    sexo=str(input('Dados inválidos. Por favor, informe seu sexo (F/M):')).upper()[0].strip()
print('Sexo {}, registrado com sucesso.'.format(sexo))
