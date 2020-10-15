a1 = int(input("Digite o primeiro termo da P.A: "))
r = int(input("Digite a razao da P.A: "))

for n in range(1, 11):
  an = a1+((n-1)*r)
  print(f"Termo {n+1} da P.A eh {an}")
