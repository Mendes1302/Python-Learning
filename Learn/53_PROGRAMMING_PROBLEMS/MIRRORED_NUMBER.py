try:
    HEX = str(input("Digite um número em HEXADECIMAL: ")).upper()


# Erros convencionais
except Exception as error:
    print(f"ERROR: {error}!!")
else:
    print("*"*30, "INIT", "*"*30)
    DEC = str(int(HEX, 16)) 
    count = 0
    div = len(DEC)//2
    for i in range(0, div):
        for k in range(len(DEC)-1, div-1, -1):
            if DEC[i] == DEC[k]:
                count += 1
    if div == count:
        print("Número é espelhado")
    else:
        print("Número não é espelhado")

print("*"*30, "END", "*"*30)
