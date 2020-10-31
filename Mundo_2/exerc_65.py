escolha = int(input("Digite [ 0 ] para sair ou um numero:"))
soma = 0
menor = maior = escolha
while escolha != 0:
    soma = escolha + soma
    if escolha > maior:
        maior = escolha
    elif escolha < menor:
        menor = escolha;
    escolha = int(input("Digite [ 0 ] para sair ou um numero:"))
print("A soma eh {}\nO maior eh {}\nO menor eh {}".format(soma, maior, menor))
