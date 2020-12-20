contador = 0
for numero in range(0,3):
    numero = int(input('Digite um numero: '))
    contador = contador + 1
    if contador == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
print(f'Esse eh o MENOR numero {menor}')
print(f'Esse eh o MAIOR numero {maior}')
