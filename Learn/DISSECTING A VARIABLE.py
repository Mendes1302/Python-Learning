tipo = input('Digite algo:')

print(f'O tipo primitivo que tu digitaste é: {type(tipo)}')
print("So tem espaco?", tipo.isspace())
print("E um numero?", tipo.isnumeric())
print("E alfabetico?", tipo.isalpha())
print("E alfanumerico?", tipo.isalnum())
print("Esta em maiuscula?", tipo.isupper())
print("Esta em minuscula?", tipo.islower())
print("Esta capilizada?", tipo.istitle())
# capitalizado é quando tem maiuscula e minuscula, exemplo: Python.
