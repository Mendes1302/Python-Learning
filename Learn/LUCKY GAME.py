from random import randint
array = list()
question = int(input("Digite quantos jogos você quer: "))
for i in range(0, question):
    for k in range(0, 6):
        aux = randint(1, 60)
        if aux in array:
            while aux in array:
                aux = randint(1, 60)
        array.append(aux)
                
    print("Meu {}º palpite é : {}".format((i+1) , sorted(array)))
    array.clear()
