from math import cos, tan, sin, radians 

angulo = float(input('Digite o angulo qualquer:'))

print(f'O cosseno eh {cos(radians(angulo)):.2f}')
print(f'A tangente eh {tan(radians(angulo)):.2f}')
print(f'O seno eh {sin(radians(angulo)):.2f}')
