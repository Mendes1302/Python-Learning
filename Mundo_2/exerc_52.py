num = int(input("Digite um numero: "))
cont = 0
for i in range(1, num+1):
  if num % i == 0:
    cont = cont + 1
if cont == 2:
  print("Ele é primo")
else:
  print("Nao é primo")
 
