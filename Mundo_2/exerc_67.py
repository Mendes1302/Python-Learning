escolha = 1
while escolha > 0:
    escolha = int(input("Digite [ -1 ] para sair ou um numero para saber a tabuada:"))
    print("="*30)
    for i in range(0,11):
        print("{} x {} = {}".format(escolha, i, i*escolha))
    print("="*30)
