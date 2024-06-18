# for, while, break, continue

# operador in

for letra in 'Python':
    print(letra)



itens = ['banana', 'arroz', 'limão']



for item in itens:
    print(item)

for i in range(5):
    print(i)

for i in range(0, 11, 2):
    print(i)


# while
contador = 0
while contador <= 5:
    print(contador)
    contador += 1

# break
# encontre o primeiro numero par
numeros = [1,3,4,5,8,11]

for numero in numeros:
    if numero % 2 == 0:
        print(numero)
        break


# continue
numeros = [3,-1,3,0,-2]
for numero in numeros:
    if numero <= 0:
        continue
    print(numero)


for numero in numeros:
    if numero > 0:
        print(numero)

# compressão de lista
# forma concisa de criar listas em python

ns = [2,3,4,5,6]
quadrados = []
for n in ns:
    quadrados.append(n ** 2)

quadrados = [n ** 2 for n in ns]
print(quadrados)

palavra = 'Olá mundo'
letras = [letra for letra in palavra]
letras = [letra.upper() for letra in palavra]
print(letras)
