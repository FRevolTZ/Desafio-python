def potenciacao(base,expoente=2):
    return base ** expoente

base = int(input('Digite a base: '))
expo = int(input('Digite o expoente (padrão: 2): '))

if expo:
    print(f"o resultado é: {potencicao(base,
    int(expo))}")
else:
    print(f"o resultado é: {potenciacao(base)}")