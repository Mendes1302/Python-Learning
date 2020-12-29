array = list()
cont = 0
aux = 'S'
while True:
    if aux in 'S':
        name = str(input("\nNome do Aluno: "))
        array.append(name)
        
        n1 = int(input("Digite a 1º nota do Aluno {}: ".format(name)))
        array.append(n1)
        
        n2 = int(input("Digite a 2º nota do Aluno {}: ".format(name)))
        array.append(n2)
    elif aux in 'N':
        print("\n")
        break;
    else:
        print("\nDigitou ERRADO !!!!, tente novamente...\n")
    
    aux = str(input("Deseja continuar? ")).upper()

for i, j in enumerate(array):
    if i == 0:
        print('Number', end=' '*10)
        print('Name', end=' '*12)
        print('Average')
        print('-'*40, '\n')
    if (i%3) == 0:
        print(cont, end=' '*15)
        print(array[i], end=' '*15)
        print((array[i+1]+array[i+2])/2, '\n')
        cont += 1
print('-'*40, '\n')

while True:
    aux = str(input("Deseja achar a nota de algum aluno? (N para sair) "))
    if aux in 'N':
        print("\n")
        break;
    else:
        if aux in array:
            idx = array.index(aux)
            print("\nAs notas do {} é 1º Nota = {} e 2º Nota = {}\n".format(aux, array[idx+1], array[idx+2]))
        else:
            print("\nDigitou ERRADO !!!!, tente novamente...\n")
