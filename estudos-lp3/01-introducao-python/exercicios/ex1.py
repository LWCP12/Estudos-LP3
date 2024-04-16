import random

def jogo_de_adivinhacao():
    numero_secreto = random.randint(1, 100)
    
    print("Tente adivinhar o número secreto entre 1 e 100.")
    
    while True:
        try:
            palpite = int(input("Digite seu palpite: "))
        except ValueError:
            print("Insira um número válido.")
            continue
        
        if palpite < numero_secreto:
            print("Seu palpite está abaixo do número secreto.")
        elif palpite > numero_secreto:
            print("Seu palpite está acima do número secreto.")
        else:
            print(f"Parabéns! Você adivinhou o número secreto: {numero_secreto}")
            break

jogo_de_adivinhacao()
