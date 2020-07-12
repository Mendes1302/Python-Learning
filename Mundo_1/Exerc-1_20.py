'''#Exercicio 1 (Hello World)
print('Hello World')

#Exercicio 2 (Escreva nome)

nome = str(input('Digite seu nome:'))
print(f'\n\nSeja bem-vindo {nome}')

#Exercicio 3 (SOMANDO DOIS NUMEROS)

print("-"*30,'SOMA',"-"*30)

a = int(input('\nDigite o primeiro numero:'))
b = int(input('\nDigite o primeiro numero:'))
soma = a + b
print(f' \n\nA soma entre {a} e {b} é {soma}')

#Exercicio 4 (DISSECANDO UMA VARIAVEL)

tipo = input('Digite algo:')

print(f'O tipo primitivo que tu digitaste é: {type(tipo)}')
print("So tem espaco?", tipo.isspace())
print("E um numero?", tipo.isnumeric())
print("E alfabetico?", tipo.isalpha())
print("E alfanumerico?", tipo.isalnum())
print("Esta em maiuscula?", tipo.isupper())
print("Esta em minuscula?", tipo.islower())
print("Esta capilizada?", tipo.istitle())
# capitalizado e quando tem maiuscula e minuscula, exemplo: Python.

#Exercicio 5 (ANTECESSOR E SUCESSOR)

numb = int(input('Digite um numero:'))
sucessor = numb + 1
antecessor = numb - 1

print(f'O numero {numb} tem como antecessor {antecessor} e sucessor {sucessor}')

#Exercicio 6 (DOBRO, TRIPLO e RAIZ QUADRADA)

from math import sqrt

numb = int(input('Digite um INTEIRO numero:'))
 
print(f'O DOBRO de {numb} eh { numb*2}')
print(f'O triplo de {numb} eh {numb*3}')
print(f'A RAIZ QUADRADA de {numb} eh {sqrt(numb)}')

#Exercicio 7 (MEDIA ARITMETRICA)

print('Escreva as duas notas do aluno para obter a media\n')
Nota1 = int(input('Primeira nota:'))
Nota2 = int(input('\nSegunda nota:'))
print(f'A media do aluno é {(Nota1+Nota2)/2}')

#Exercicio 8 (CONVERSOR DE MEDIDA)

medida_em_metros = int(input('Digite uma medida em metros:'))
print(f'A medida de {medida_em_metros}m eh igual a:')
print(f'{medida_em_metros*100}cm')
print(f'{medida_em_metros*1000}cm')

#Exercicio 9 (TABUADA)

numb = int(input('Digite um INTEIRO numero:'))

print("="*30, 'TABUADA',"="*30)
for m in range(0, 11):
    print(f'{numb} x {m} = {numb*m}')
print("="*30, 'FIM',"="*30)

#Exercicio 10 (CONVERSOR DE MOEDA)

dinheiro = float(input('Digite um valor em reais:'))
print(f'Com R${dinheiro:.2f} voce tera U${dinheiro/5.34:.2f}')

#Cotação do dólar está 1 para 5.34// 11/07/2020 as 18h33


#Exercicio 11 (PINTANDO PAREDE)

altura = float(input('Digite a altura da parede:'))
largura = float(input('Digite a largura da parede:'))

print(f'A parede precisara de {(altura*largura)/2:.2f} litros de tinta, pois sua area é de {altura*largura:.2f}M^2')

#Exercicio 12 (CALCULANDO DESCONTO) 

preco = float(input('Digite o valor do produto:'))
print(f'O produto por ter um desconto de 5% seu novo valor eh de R${preco*0.95:.2f}')

#Exercicio 13 (REAJUSTE DE SALARIO)

salario = float(input('Digite o valor do salario:'))
print(f'O salario por ter um aumento de 15% seu novo valor eh de R${salario*1.15:.2f}')

#Exercicio 14 (CONVERSOR DE TEMPERATURA)

celsius = float(input('Digite a temperatura em graus celsius:'))
print(f'A temperatura de {celsius} graus celsius eh igual a {((celsius/5)*9)+32:.2F}')

#Exercicio 15 (ALUGUEL DE CARROS)

quant_km = float(input('Digite a quantidade de KM percorrido pelo carro:'))
quant_dia = float(input('Digite a quantidade de dias percorrido com o carro:'))
print(f'O valor a ser pago eh R${(quant_km*0.15)+(quant_dia*60):.2f}')

#Exercicio 16 (QUEBRANDO UM NUMERO)

numb = float(input('Digite um numero:'))
if numb < 0:
    print(f'O numero nao tem porcao inteira')
else:

#Exercicio 17 (CATETOS E HIPOTENUSA)

from math import sqrt

cateto_oposto = int(input('Digite o valor do cateto oposto:'))
cateto_adjacente = int(input('Digite o valor do cateto adjacente:'))

print(f'O valor da hipotenusa eh {sqrt((cateto_oposto**2)+(cateto_adjacente**2)):.2f}')

#Exercicio 18 (SENO, COSSENO e TANGENTE)

from math import cos, tan, sin, radians 

angulo = float(input('Digite o angulo qualquer:'))

print(f'O cosseno eh {cos(radians(angulo)):.2f}')
print(f'A tangente eh {tan(radians(angulo)):.2f}')
print(f'O seno eh {sin(radians(angulo)):.2f}')'''

#Exercicio 19 (SORTEANDO UM ITEM NA LISTA)

from random import randint

lista_nomes = list()
for n in range(0,4):
    lista_nomes.append[n](int(input('Digite o nome do aluno:')))

print(f'O sorteado foi {randint(lista_nomes)}')


