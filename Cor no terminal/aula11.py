print('\033[0;30;41mOlá,mundo!')
print('\033[7;35;44mOlá,mundo!')
print('\033[4;32;44mOlá,mundo!')
print('\033[1;35;43mOlá,mundo!')
print('\033[30;42mOlá,mundo!')
print('\033[mOlá,mundo!')
print('\033[7;30mOlá,mundo!')
    # \033[7;35;44m
    # \033[0;30;41m
    # \033[4;32;44m
    # \033[1;35;43m
    # \033[30;42m
    # \033[m
    # \033[7;30m
    # style 
    # 0 - simples
    # 1 - bold
    # 4 - sublinhado
    # 7 - destaque
    # text
    # 30 - branco
    # 31 - vermelho
    # 32 - verde
    # 33 - amarelo
    # 34 - azul
    # 35 - roxo
    # 36 - azul
    # 37 - cinza
    # back
    # 40 - branco
    # 41 - vermelho
    # 42 - verde
    # 43 - amarelo
    # 44 - azul
    # 45 - roxo
    # 46 - azul
    # 47 - cinza
nome="Rosa"
print("Olá, muito prazer em te conhecer {}{}{}!!!".format('\033[0;30;41m',nome,'\033[m'))