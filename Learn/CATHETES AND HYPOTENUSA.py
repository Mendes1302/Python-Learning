from math import sqrt

cateto_oposto = int(input('Digite o valor do cateto oposto:'))
cateto_adjacente = int(input('Digite o valor do cateto adjacente:'))

print(f'O valor da hipotenusa eh {sqrt((cateto_oposto**2)+(cateto_adjacente**2)):.2f}')
