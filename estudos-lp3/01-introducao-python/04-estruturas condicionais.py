# if
idade = 20

if idade >= 18:
    print('Maior de Idade')

# if/else
if idade >= 18:
    print('Maior de idade')
else:
    print('Menor de idade')

# if/elif/else
# operador ternário

idade = 20

if idade >=10:

    status = 'Maior de idade'
else:
    status = 'Menor de idade'

status = 'Menor de idade' if idade >= 18 else 'Menor de idade'

# match case
# python 3.10
dia = 3
match dia: 
    case 1:
        print('Domingo')
    case 2:
        print('Segunda')
    case 3:
        print('Terça')
    case _:
        print('Inválido')

# imprimir
# 1 e 7 - fim de semana
# 2, 3, 4, 5, 6 - dia útil

match dia:
    case 1 | 7:
        print('Fim de semana')
    case 2 | 3 | 4 | 5 | 6:
        print('Dia útil')
    case _:
        print('Dia inválido')
    


















