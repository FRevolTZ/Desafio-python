capitais = {
    'Brasil': 'brasilia',
    'Argentina': 'buenos aires',
    'Canada': 'otawwa',
    'Italia': 'roma',
    'EUA': 'washington'
}

digitado = input('Digite o nome de um país: ')

if digitado in capitais:
    print(f'a capital de {digitado} é {capitais[digitado]}')
else:
    print(f'nao temos informaçoes da capital de {digitado}')


