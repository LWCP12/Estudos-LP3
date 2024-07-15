def calc_imc(peso, altura):
    return peso / (altura ** 2)

def classifica_imc(imc):
    if imc < 18.5:
        return "Baixo peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Excesso de peso"
    elif imc < 35:
        return "Obesidade de Classe 1"
    elif imc < 40:
        return "Obesidade de Classe 2"
    else:
        return "Obesidade de Classe 3"

def peso_ideal(altura):
    return 24.9 * (altura ** 2)

def main_imc():
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))
    
    imc = calc_imc(peso, altura)
    classificacao = classifica_imc(imc)
    peso_ideal_valor = peso_ideal(altura)
    
    print(f"Seu IMC é: {imc:.2f}")
    print(f"Classificação: {classificacao}")
    
    if classificacao != "Peso normal":
        if imc < 24.9:
            peso_necessario = peso_ideal_valor - peso
            print(f"Você precisa ganhar {peso_necessario:.2f} kg para atingir o peso normal.")
        else:
            peso_necessario = peso - peso_ideal_valor
            print(f"Você precisa perder {peso_necessario:.2f} kg para atingir o peso normal.")

main_imc()
