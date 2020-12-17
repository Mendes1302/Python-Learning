control = 'S'
cont = 0
array = list()
print("\n" , "="*30, "BEGIN", "="*30)
while control in "Ss":
    value = int(input("\nDigite um valor: "))
    if cont == 0:
        array.append(value)
    else:
        if(value in array):
                print("VALOR DUPLICADO")
        else:
            array.append(value)
    cont = cont + 1    
    control  = str(input("\nDeseja continuar [S/N]: "))
print(sorted(array))
print("\n" , "="*30, "END", "="*30)
