work = dict()

work["Nome"] = str(input("Nome: "))
work["Nascimento"] = int(input("Ano de nascimento: "))
work["CTPS"] = int(input("Nº da carteira de trabalho (0 PARA NÃO): "))

if work["CTPS"] == 0:
    print("\n     NÃO É POSSÍVEL FAZER A SIMULAÇÃO, POIS NÃO TEM CTPS!!!!!\n")
else:
    work["Ano"] = int(input("Ano de contribuição: "))
    work["Salário"] = int(input("Salário: "))
    work["Aposentadoria"] = f"de tempo estimado {(35+work['Ano'])}"

print()
for k, v in work.items():
    print(f"    {k} possui o valor {v}")
