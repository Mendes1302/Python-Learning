numb = int(input('Digite um numero:[ENTRE 0 a 9999]\n'))

milhar = numb // 1000 % 10
centena = numb // 100 % 10
dezena = numb // 10 % 10
unidade = numb//1 % 10

print(f'Ha {milhar} milhar')
print(f'Ha {centena} centena')
print(f'Ha {dezena} dezena')
print(f'Ha {unidade} unidade')
