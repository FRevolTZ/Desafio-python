cidades = ("Florianópolis", "Palhoça", "Porto Alegre")

digitado = input("Digite o nome da cidade: ")

if digitado in cidades:
    print(f"{digitado} está na lista cidades")
else:
    print(f"{digitado} não está na lista cidades")


