numeros = [1,2,3,4,5]
quadrado = lambda x: x ** 2

resultado = []
for i in numeros:
    resultado.append(quadrado(i))

print(f'Os quadrados de {numeros} e igual a {resultado}')