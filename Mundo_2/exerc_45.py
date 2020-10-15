import random
print("+"*30, "JOGO PEDRA, PAPEL ou TESOURA","+"*30)
escolha = 0

while escolha != -1:
  print("\nEscolha uma das opcoes\n")
  print("[ 0 ] PEDRA")
  print("[ 1 ] PAPEL")
  print("[ 2 ] TESOURA")
  print("[ -1 ] FIM")
  escolha = int(input("\nSua escolha: "))
  computador = random.randint(0,2)
  
  if computador == escolha:
    print(f"\nEscolheram o mesmo {escolha}");
  else:
    if computador == 2 and escolha == 1:
      print(f"\nVoce escolheu {escolha} e o computador {computador},portanto ele ganhou");
    elif computador == 2 and escolha == 0:
      print(f"\nVoce escolheu {escolha} e o computador {computador},portanto voce ganhou");
    elif computador == 1 and escolha == 0:
      print(f"\nVoce escolheu {escolha} e o computador {computador},portanto ele ganhou");
    elif computador == 1 and escolha == 2:
      print(f"\nVoce escolheu {escolha} e o computador {computador},portanto voce ganhou");
    elif computador == 0 and escolha == 1:
      print(f"\nVoce escolheu {escolha} e o computador {computador},portanto voce ganhou");
    elif computador == 0 and escolha == 2:
      print(f"\nVoce escolheu {escolha} e o computador {computador},portanto ele ganhou");
