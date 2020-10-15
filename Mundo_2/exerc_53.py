frase = str(input("Digite uma frase: ")).strip()
var = 0
for i in range(1, (len(frase))+1):
  if frase[i-1] == frase[len(frase)-i]:
    var = var + 1
if var == len(frase):
  print("Frase e polindromo")
