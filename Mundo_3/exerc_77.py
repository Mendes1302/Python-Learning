tupla = ('Lucas', 'Lapis', 'Notebook', 'Faculdade', 'Python')

for palavra in tupla: 
    print(f'\nNa palavra {palavra.upper()} temos ', end='')
    for letras in palavra:
        if letras.lower() in 'aeiou':
            print(f'{letras}', end=' ')
