reta1 = float(input('Digite o valor da reta1: '))
reta2 = float(input('Digite o valor da reta2: '))
reta3 = float(input('Digite o valor da reta3: '))

if reta1 + reta2 > reta3 and reta3 + reta2 > reta1 and reta1 + reta3 > reta2:
    print('Com esses retas pode-se formar um triangulo')
else:
    print('Com esses retas nao pode formar um triangulo')
