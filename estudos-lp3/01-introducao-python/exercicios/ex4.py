votos = {
    1: 0,  
    2: 0,  
    3: 0   
}

def votar():
    print("\nSelecione um candidato para votar:")
    print("1. Candidato A")
    print("2. Candidato B")
    print("3. Candidato C")

    while True:
        try:
            escolha = int(input("Digite o número que corresponde ao candidato (1, 2 ou 3): "))
            if escolha in [1, 2, 3]:
                return escolha
            else:
                print("Escolha inválida. Digite um número entre 1 e 3.")
        except ValueError:
            print("Entrada inválida.")

def main():
    try:
        num_votos = int(input("Quantas vezes você deseja votar? "))
    except ValueError:
        print("Entrada inválida.")
        return
    
    # Coleta os votos
    for _ in range(num_votos):
        escolha = votar()
        votos[escolha] += 1
    
    # Exibe o número de votos de cada candidato
    print("\nResultado da votação:")
    print(f"Candidato A: {votos[1]} votos")
    print(f"Candidato B: {votos[2]} votos")
    print(f"Candidato C: {votos[3]} votos")
    
    # Determina o vencedor com base no maior número de votos
    vencedor = max(votos, key=votos.get)
    
    # Exibe o vencedor
    print(f"\nO vencedor é o Candidato {'ABC'[vencedor - 1]} com {votos[vencedor]} votos!")

main()
