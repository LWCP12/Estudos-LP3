# Tipos de dados

# 1. Númerico
# int, float, complex

# int
idade = 10
temperatura = -30

# float
altura = 178.30

# 2. Bool
verdade = True
falso = False

# 3. String
# sequência de caracteres
nome = 'Marcos Leonardo'
nome = "Giusepe Cadura"

# multilinhas
frase = """Socorro!
alguém me ajuda!
por favor!
"""

# interpolação de string
# f-strings
nome = "Jonas Camargo"
idade = 20
frase = f"Olá {nome}, Você tem {idade} anos!"
print(frase)

# char
letra = 'a'
letra = "a"

# acesso um caractere da string
nome = "João Bito"
print(nome[0])
print(nome[-1])
print(nome[-3])

# strings são objetos
# métodos

print(nome.capitalize()) # João bito
print(nome.upper()) # JOÃO BITO

# 4. list (listas)
# lista de valores
# indexada 
# pode ser alterada

frutas = []
frutas = ['melancia', 'banana', 'morango']

# acessar um item da lista 
frutas[1]

# adicionar um item na lista
frutas.append('goiaba') # melancia, banana, morango, goiaba

# inserir em uma posição
# forma 1
frutas.insert(2,'kiwi')
print(frutas)

# forma 2
frutas.clear()
print(frutas)

#forma 3
for fruta in frutas:
    print(fruta)

# 5. tuple (tupla)
# 'lista' de valores
# não pode ser alterada
opcoes = ('sim', 'nao', 'talvez')

print(opcoes[0])
for opcao in opcoes:
    print(opcoes)

# set(conjunto)
# conjunto de valores
# não permite elementos duplicados
# não é indexado
habilidades = {'java', 'c', 'python'}
print(habilidades)

# dict (dicionario)
# palavra -> definição
# chave -> valor
# key -> value
# conjunto chave valor

nome = "Mateus Bastos"
idade = 17
skills = ['java', 'c']
empregado = True

candidato = {
    'nome': 'Mateus Bastos',
    'idade': 17,
    'skills': ['java', 'c'],
    'empregado': True
}

print(candidato['nome'])
print(candidato.keys())
print(candidato.values())

# 7. None
nome = None


print(" CASE 2: When we need to take multiple input in Python")
#print statement

s,t,u = [int(s) for s in input("Please enter values for variables ").split()]
# assigning values in a single line for three variables s, t, and u and implementing a list comprehension method to obtain individual values
print("The value for variables are :", s,t,u)
# printing the three variables

a,b,c = [int(a) for a in input("Please enter values for variables ").split(",")]
# assigning values in a single line for three variables a, b and c and implementing a list comprehension method to obtain individual values
print("The value for variables are :", a,b,c)
# printing the three variables

print(" CASE 3: When we need to take Multiple Inputs using separator:")
#print statement

k = [int(k) for k in input("Please enter two values for variables ").split(",")]
# assigning values in a single line for three variables a, b and c and implementing a list comprehension method to obtain individual values
print("The value for variables are :", k)
# printing the three variables