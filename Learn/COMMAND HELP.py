def help_for_help(resp):
    
    print("Acessando o manual de '{}':".format(resp))
    print("    {}".format(help(resp)))


while True:
    resp = str(input(" Digite uma função para saber a descrição ou FIM para sair: "))
    
    if resp.upper() in "FIM":
        break
    else:
        help_for_help(resp)
