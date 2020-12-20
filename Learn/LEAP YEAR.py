ano = float(input('Digite um ano para saber se ele eh BISSEXTO:'))

if ano % 4 == 0 and ano % 100 != 0:
    print(f'O ano de {ano:.0F} eh BISSEXTO')
else:
    print(f'O ano de {ano:.0F} nao eh BISSEXTO')
