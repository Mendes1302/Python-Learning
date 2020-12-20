distancia = float(input('Digite a distancia da viagem [em KM]:'))

if distancia >= 200:
    print(f'O valor da viagem sera de R${distancia*0.45:.2f}')
else:
    print(f'O valor da viagem sera de R${distancia*0.5:.2f}')
