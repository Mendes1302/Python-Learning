valor = int(input("Digite o valor para sacar:"))
resto = 1
cont50 = cont20 = cont10 = cont1 = 0
print("O valor de R$ {} terá".format(valor))
while resto != 0:
    if valor >= 50:
        resto = valor % 50
        cont50 = valor / 50 
    elif valor >= 20 and valor < 50:
        resto = valor % 20
        cont20 = valor / 20
    elif valor >= 10 and valor < 20:
        resto = valor % 10
        cont10 =valor / 10
    elif valor >= 1and valor < 10:
        resto = valor % 1
        cont1 = valor / 1
    valor = resto
print("{:.0f} x R$ 50 reais\n{:.0f} x R$ 20 reais".format(cont50, cont20))
print("{:.0f} x R$ 10 reais\n{:.0f} x R$ 1 reais".format(cont10, cont1))
