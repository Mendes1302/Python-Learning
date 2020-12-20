frase = str(input('Escreva uma frase: ')).upper()

print(f'Aparece {frase.count("A")} vezes a letra A')
print(f'Aparecendo na posicao {frase.find("A")+1} a letra A pela primeira vez')
print(f'Aparecendo na posicao {frase.rfind("A")} a letra A pela ultima vez')
