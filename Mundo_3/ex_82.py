numeros = list()
par = list()
impar = list()
controle = 's'
while controle in 'Ss':
    number = int(input("\nDigite um valor: "))
    if (number % 2) == 0:
        par.append(number)
        numeros.append(number)
    else:
        impar.append(number)
        numeros.append(number)    
    controle = str(input("\nDeseja continuar[S/N]: "))
print("Essa é a lista dos numeros gerias:", sorted(numeros))
print("Essa é a lista dos numeros pares:", sorted(par))
print("Essa é a lista dos numeros impares:", sorted(impar))
