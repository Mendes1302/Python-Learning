lista = list()


for pos in range(0, 1):
    valor = int(input("Digite uma valor: "))
    if pos == 0:
        maior = menor = valor
    if valor > maior:
        maior = valor
    elif valor < menor:
        menor = valor
    lista.append(valor)
print(lista)
print(f"O maior é {maior} pos = {(lista.index(maior))+1}\nO menor é  {menor} pos = {(lista.index(menor))+1}\n")
