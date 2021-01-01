
def fatorial(number, condition = False):
    """
    Função para calculo de fatorial:
    
    :param number: partida da fatorial
    :param condition: True mostra o processo
    """
    f = 1
    for i in range(number, 1, -1):
        if condition:
            f *= i
            if i == 2:
                break
            print(f)
        else:
            f *= i
            
    print(f)

fatorial(5)
print()
fatorial(6, True)
help(fatorial)
