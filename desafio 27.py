def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n-1)

user = int(input('Digite um numero: '))
print(f'o fatorial de {user} é {fatorial(user)}')