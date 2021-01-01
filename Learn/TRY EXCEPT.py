def readINT(txt):
    while True:
        try:
           n = int(input(txt))
        except (ValueError, TypeError):
            print("\033[31mDigite um número INTEIRO valor válido\033[m")
            continue
        else:
            return n
        finally:
            print()
        


num =  readINT("Digite um valor INTEIRO: ")
print(f"O valor inteiro é {num}")
print('-'*30, 'FIM', '-'*30)
