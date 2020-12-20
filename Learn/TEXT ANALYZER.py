nome = str(input('Escreva seu nome:'))

print(f'Seu nome com todas as letras maiusculas: {nome.upper()}')
print(f'Seu nome com todas as letras minusculas: {nome.lower()}')
print(f'A quantidade de letras no seu nome eh: {len(nome) - nome.count(" ")}')
separa = nome.split()
print(f'A quantidade de letras do seu primeiro nome eh : {len(separa[0])}')
