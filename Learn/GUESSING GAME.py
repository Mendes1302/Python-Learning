from random import randint

computador = randint(0,5)
pessoa = int(input('Escreva um número: [entre 0 e 5]'))
if computador == pessoa:
    print(f'Voce ACERTOU pois o computador escolheu {computador} e voce {pessoa}')
else:
    print(f'Voce ERRO pois o computador escolheu {computador} e voce {pessoa}')
