print("="*30,"[Conversao de BASES]","="*30)

escolha = 0

while escolha != 4:
    value = int(input("Digite um valor para a conversao: "))
    print("\nEscolha uma das opcoes:\n")
    print("[ 1 ] Conversao do numero em HEXADECIMAL.")
    print("[ 2 ] Conversao do numero em OCTAL.")
    print("[ 3 ] Conversao do numero em BINARIO.")
    print("[ 4 ] FIM.")

    escolha = int(input("\nSua escolha: "))
    if escolha == 1:
        print(f"\nO valor {value} em HEXADECIMAL eh {hex(value)}")
    elif escolha == 2:
        print(f"\nO valor {value} em OCTAL eh {oct(value)}")
    elif escolha == 3:
        print(f"\nO valor {value} em BINARIO eh {bin(value)}")
    elif escolha == 4:
        print("="*30,"[F I M]","="*30)
    else:
        print("\nERROR in system")
