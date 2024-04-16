import random

def escolher_palavra():
    # Lista de palavras para o jogo
    palavras = ["socorro", "sunga", "pedregulho", "algas", "mercurio", "pizza", "animais", "metal", "guitarra", "espaco"]
    # Escolhe uma palavra aleatoriamente da lista
    return random.choice(palavras)

def jogo_da_forca():
    palavra = escolher_palavra()
s
   tentativas_restantes = 6

    palavra_oculta = ['_' for _ in palavra]
s
    letras_adivinhadas = set()
    
    print("Bem-vindo ao Jogo da Forca!")

    while tentativas_restantes > 0:
        print("\nPalavra: ", ' '.join(palavra_oculta))
        
        print("Letras já adivinhadas: ", ' '.join(sorted(letras_adivinhadas)))

        palpite = input("Digite uma letra para adivinhar: ").lower()

        if palpite in letras_adivinhadas:
            print("Você já adivinhou essa letra. Tente outra.")
            continue
        
        letras_adivinhadas.add(palpite)

        if palpite in palavra:
            print("Boa! A letra está na palavra.")
            
            for index, char in enumerate(palavra):
                if char == palpite:
                    palavra_oculta[index] = palpite
            if '_' not in palavra_oculta:
                print("\nParabéns! Você adivinhou a palavra: ", palavra)
                break
        else:
            tentativas_restantes -= 1
            print(f"Letra incorreta! Você tem {tentativas_restantes} tentativas restantes.")
        
        if tentativas_restantes == 0:
            print(f"\nVocê perdeu! A palavra era: {palavra}")

jogo_da_forca()

