soma = 0
cont = 0
for i in range (1, 501):
  if (i % 2) != 0 and (i % 3) == 0:
    cont = cont + 1
    soma = soma + i
print(f"O valor da soma dos {cont} valores eh {soma}")
    
