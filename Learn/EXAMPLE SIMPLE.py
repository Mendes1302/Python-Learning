classroom = dict()

classroom["NAME"] = str(input("Nome: "))
classroom["AVG"] = int(input(f"Média de {classroom['NAME']}: "))

if classroom["AVG"] >= 7:
    print("\nAluno APROVADO!!!")
else:
    print("\nAluno REPROVADO!!")
print()
