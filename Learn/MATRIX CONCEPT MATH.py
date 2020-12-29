soma = soma_peer = soma_row_3 = maior = 0
matriz = list()
for i in range(1, 4):
    for j in range (1, 4):
        matriz.append(int(input("Digite um valor para [{}, {}]: ".format(i , j))))
        
for k, i in enumerate(matriz):
    soma = soma + i
    
    
    if (k%3) == 0:
        soma_row_3 = soma_row_3 + matriz[k-1]
        print("\n")
        
    if (i%2) == 0:
        soma_peer = soma_peer + i
        
    if i in matriz[3:6]:
        if i > maior:
            maior = i
    print("[ {} ] ".format(matriz[k]), end='')
print("\n")
print("Na matriz (3, 3) tem a SOMA dos valores: {}".format(soma))
print("Na matriz (3, 3) tem a SOMA dos pares: {}".format(soma_peer))
print("Na matriz (3, 3) tem a SOMA da coluna 3: {}".format(soma_row_3))
print("Na matriz (3, 3) tem o MAIOR valor da linha 2: {}".format(maior))
