try:
    N = int(input("Digite um número inteiro sendo (1< N< 1000): "))

# Erros convencionais
except Exception as error:
    print(f"ERROR: {error}!!")
if N >= 1000:
    raise Exception(f"ERROR: Number greater than the condition!!")
if N <= 1:
    raise Exception(f"ERROR: Number less than the condition!!")
else:
    print("*"*30, "INIT", "*"*30)
    sum_dec = sum_hex = sum_oct = 0
    for i in range(N+1):
        sum_dec += i
        if i % 2 == 0:
            sum_hex += i
        else:
            sum_oct += i

    print(f"VALUE: {N}")

    print(f"SOMA EM DECIMAL: {sum_dec}")
    x = hex(sum_hex).upper()
    print(f"SOMA EM HEXADECIMAL: {x[2:]}")
    x = oct(sum_oct)
    print(f"SOMA EM OCTAL: {x[2:]}")

print("*"*30, "END", "*"*30)
