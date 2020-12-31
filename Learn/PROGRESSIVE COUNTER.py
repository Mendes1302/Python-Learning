from time import sleep

def contagem(init, end, reason):
    print()
    print(f"Contagem de {init} até {end} de {reason} em {reason}:")
    for value in range(init, end+1, reason):
        print(f"{value} ", end="")
        sleep(0.5)
    print("\nFIM")
    
    print(f"Contagem de {end} até {init} de {reason} em {reason}:")
    for value in range(end, init-1, -reason):
        print(f"{value} ", end="")
        sleep(0.5)
    print("\nFIM")


init = int(input("INIT: ")) 
end = int(input("END: ")) 
reason = int(input("REASON: ")) 

contagem(init, end, reason)
