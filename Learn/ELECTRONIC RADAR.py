velocidade = float(input('Digite a velocidade do carro[em KM/h]:'))

if velocidade > 80:
    print(f'Voce ultrapassou a velocidade permitida de 80km/h, portanto pagara uma multa de R${(velocidade-80)*7:.2f}')
else:
    print(f'Continue!! Mas nao ultrapasse a velocidade de 80km/h')
