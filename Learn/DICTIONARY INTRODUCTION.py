states = dict()
brazil = list()

for c in range(0, 2):
    states['UF'] = str(input("Unidade federativa: "))
    states["SIGLA"] = str(input("Sigla do Estado: "))
    brazil.append(states.copy())

for e in brazil:
    for k, v in e.items():
        print(f"{v}", end=' ')
    print()
classroom = dict()

classroom["NAME"] = str(input("Nome: "))
classroom["AVG"] = int(input(f"Média de {classroom['NAME']}: "))

if classroom["AVG"] >= 7:
    print("\nAluno APROVADO!!!")
else:
    print("\nAluno REPROVADO!!")
print()
