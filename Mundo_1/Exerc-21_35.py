#Exercicio 21 (SORTEANDO UMA ORDEM  NA LISTA)

import pygame

pygame.init()
pygame.mixer.music.load('colocar end do mp3')
pygame.mixer.music.play()
pygame.even.wait()

#Exercicio 22 (ANALIZADOR DE TEXTOS)

nome = str(input('Escreva seu nome:'))

print(f'Seu nome com todas as letras maiusculas: {nome.upper()}')
print(f'Seu nome com todas as letras minusculas: {nome.lower()}')
print(f'A quantidade de letras no seu nome eh: {len(nome) - nome.count(" ")}')
separa = nome.split()
print(f'A quantidade de letras do seu primeiro nome eh : {len(separa[0])}')

#Exercicio 23 (SEPARANDO DIGITOS DE UM NUMERO)

numb = int(input('Digite um numero:[ENTRE 0 a 9999]\n'))

milhar = numb // 1000 % 10
centena = numb // 100 % 10
dezena = numb // 10 % 10
unidade = numb//1 % 10

print(f'Ha {milhar} milhar')
print(f'Ha {centena} centena')
print(f'Ha {dezena} dezena')
print(f'Ha {unidade} unidade')

#Exercicio 24 (VERIFICANDO A PRIMEIRA LETRA DE UM TEXTO)

cidade = str(input('Escreva o nome da sua cidade:'))
print(cidade[:5].upper() == 'SANTO')

#Exercicio 25 (PROCURANDO UMA STRING DENTRO DE OUTRA)

nome = str(input('Qual eh seu nome completo ?')).strip()
print(f'Seu nome tem SILVA? {"silva" in nome.lower()}')

#Exercicio 26 (PRIMEIRA E ULTIMA OCORRENCIA DE UMA STRING)

frase = str(input('Escreva uma frase: ')).upper()

print(f'Aparece {frase.count("A")} vezes a letra A')
print(f'Aparecendo na posicao {frase.find("A")+1} a letra A pela primeira vez')
print(f'Aparecendo na posicao {frase.rfind("A")} a letra A pela ultima vez')

#Exercicio 27 (PRIMEIRO E ULTIMO NOME DE UMA PESSOA)

n = str(input('Escreva seu nome completo: ')).strip()
nome = n.split()
print(f'Seu primeiro nome eh {nome[0]}')
print(f'Seu ultimo nome eh {nome[len(nome)-1]}')

#Exercicio 28 (JOGO DE ADIVINHACAO V.10)

from random import randint

computador = randint(0,5)
pessoa = int(input('Escreva um número: [entre 0 e 5]'))
if computador == pessoa:
    print(f'Voce ACERTOU pois o computador escolheu {computador} e voce {pessoa}')
else:
    print(f'Voce ERRO pois o computador escolheu {computador} e voce {pessoa}')
    

#Exercicio 29 (RADAR ELETRONICO)

velocidade = float(input('Digite a velocidade do carro[em KM/h]:'))

if velocidade > 80:
    print(f'Voce ultrapassou a velocidade permitida de 80km/h, portanto pagara uma multa de R${(velocidade-80)*7:.2f}')
else:
    print(f'Continue!! Mas nao ultrapasse a velocidade de 80km/h')


#Exercicio 30 (PAR OU IMPAR?)

numb = int(input('Digite um numero INTEIRO:'))

if numb % 2 == 0:
    print(f'O numero {numb} eh PAR')
else:
    print(f'O numero {numb} eh IMPAR')

#Exercicio 31 (CUSTO DA VIAGEM)

distancia = float(input('Digite a distancia da viagem [em KM]:'))

if distancia >= 200:
    print(f'O valor da viagem sera de R${distancia*0.45:.2f}')
else:
    print(f'O valor da viagem sera de R${distancia*0.5:.2f}')

#Exercicio 32 (ANO BISSEXTO)

ano = float(input('Digite um ano para saber se ele eh BISSEXTO:'))

if ano % 4 == 0 and ano % 100 != 0:
    print(f'O ano de {ano:.0F} eh BISSEXTO')
else:
    print(f'O ano de {ano:.0F} nao eh BISSEXTO')

#Exercicio 33 (MAIOR E MENOR VALOR)

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


#Exercicio 34 (REAJUSTE DE SALARIO 2.0)

salario = float(input('Digite o valor do salario:'))
if salario > 1250:
    print(f'O salario por ter um aumento de 10% seu novo valor eh de R${salario*1.10:.2f}')
else:
    print(f'O salario por ter um aumento de 15% seu novo valor eh de R${salario*1.15:.2f}')
 
 #Exercicio 35 (ANALISANDO UM TRIANGULO 1.0)

reta1 = float(input('Digite o valor da reta1: '))
reta2 = float(input('Digite o valor da reta2: '))
reta3 = float(input('Digite o valor da reta3: '))

if reta1 + reta2 > reta3 and reta3 + reta2 > reta1 and reta1 + reta3 > reta2:
    print('Com esses retas pode-se formar um triangulo')
else:
    print('Com esses retas nao pode formar um triangulo')