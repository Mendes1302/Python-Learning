numero = int(input("Digite um numero: "))
fatorial = 1
print(f"\n{numero}! = ", end='')
for i in range(numero, 0, -1):
  fatorial = fatorial*i
  if i == 1:
    print(i, end='')
  else:
    print(i, "x ",end='')

print(f' = {fatorial}')
