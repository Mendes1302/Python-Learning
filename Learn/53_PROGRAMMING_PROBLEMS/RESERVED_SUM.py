def Rev(aux):
    x = int(aux[::-1])
    return x
M = str(input("Digite um valor inteiro: "))
N = str(input("Digite outro valor inteiro: "))

soma = str(Rev(N)+Rev(M))
soma = str(Rev(soma))

print(soma)