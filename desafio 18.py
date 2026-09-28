carros = ['BMW X6', 'BMW i5', 'BMW i8']
pesquisa = input('qual carro voce deseja pegar? ')

if pesquisa in carros:
    print("Este carro está disponível")
else:
    print("Desculpe, este carro não está disponivel")