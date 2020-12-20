salario = float(input('Digite o valor do salario:'))
if salario > 1250:
    print(f'O salario por ter um aumento de 10% seu novo valor eh de R${salario*1.10:.2f}')
else:
    print(f'O salario por ter um aumento de 15% seu novo valor eh de R${salario*1.15:.2f}')
