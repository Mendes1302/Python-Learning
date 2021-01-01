from random import randint

def create(number):
    """
    -> CRIAR ELEMENTOS ALEATORIOS DE UMA LISTA
    :param number: lista.
    :return: NOT
    """
    for i in range(0, 10):
        number.append(randint(0,60))
    print(number)

def SUM(a, b, c=0):
    print(a+b+c)
        

number = list()

help(create)
create(number)

SUM(2, 4)
