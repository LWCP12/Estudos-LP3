def exibir_tabuada(numero):
    for multiplicador in range(1, 11):
        resultado = numero * multiplicador
        print(f'{numero} x {multiplicador} = {resultado}')

numero = int(input('Digite um número inteiro para mostrar sua tabuada:\n'))

exibir_tabuada(numero)
