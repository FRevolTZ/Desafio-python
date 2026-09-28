par_impar = lambda n: 'par' if n%2==0 else 'impar'

user = int(input('Digite um numero: '))
print(f'o numero {user} é {par_impar(user)}')