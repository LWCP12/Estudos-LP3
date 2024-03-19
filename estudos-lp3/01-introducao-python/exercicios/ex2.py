#Ex2 - Escreva um programa que solicita ao usuário 3 notas e apresenta a média aritmética

n1,n2,n3 = [int(n1) for n1 in input("Coloque as três notas ").split()]
print("As notas são", n1,n2,n3)
m = (n1 + n2 + n3)/3
print(m)