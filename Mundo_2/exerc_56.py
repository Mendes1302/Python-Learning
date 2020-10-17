tam = 2
maior = 0
mulher20 = 0
soma_idade = 0
y = 0;

vetor_nome = [0]*tam
vetor_idade = [0]*tam
vetor_sexo = [0]*tam

for i in range(0, tam):
  vetor_nome[i] = str(input(f"\nDigite o nome da {i+1} pessoa: ")).lower()
  vetor_sexo[i] = str(input(f"Digite o sexo da {i+1} pessoa [M/F]: ")).lower()
  vetor_idade[i] = int(input(f"Digite a idade da {i+1} pessoa:"))
  soma_idade = vetor_idade[i] + soma_idade
  if vetor_sexo[i] in 'f':
    if vetor_idade[i] < 20:
      mulher20 = mulher20 + 1
  elif vetor_sexo[i] in 'm':
    if vetor_idade[i] > maior:
      maior = vetor_idade[i]
      y = i
  else:
    print("\nERRO")
    break;
print(f"\nA media de idade eh {soma_idade/tam}")
print(f"\nHa {mulher20} mulheres com menos de 20 anos de idade")
print(f"\nO homem mais velho tem {vetor_idade[y]} anos e se chama {vetor_nome[y]}")
