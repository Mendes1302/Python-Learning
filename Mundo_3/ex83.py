expressao = str(input("\nDigite uma expressao: "))
if expressao.count("(") == expressao.count(")"):
    print("Expressao correta :)")
else:
    print("Expressao incorreta :(")
