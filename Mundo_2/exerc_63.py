num = int(input("Digite um numero: "))
p2 = 0
p1 = 1
soma = 0
if num > 2:
  print("0\n1")
  for i in range(2,num):
    soma = p1 + p2;
    print(f"{soma}")
    p2 = p1
    p1 = soma
elif num == 2:
  print("0\n1")
else:
  print("0")
