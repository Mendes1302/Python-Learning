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

