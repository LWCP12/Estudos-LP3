def calc_volume(comprimento, altura, largura):
    return (comprimento * altura * largura) / 1000

def calc_potencia_termometro(volume, temp_desejada, temp_ambiente):
    return volume * 0.05 * (temp_desejada - temp_ambiente)

def calc_filtragem(volume):
    return volume * 2, volume * 3

def main_aquario():
    comprimento = float(input("Digite o comprimento do aquário (cm): "))
    altura = float(input("Digite a altura do aquário (cm): "))
    largura = float(input("Digite a largura do aquário (cm): "))
    temp_desejada = float(input("Digite a temperatura desejada (°C): "))
    temp_ambiente = float(input("Digite a temperatura ambiente (°C): "))
    
    volume = calc_volume(comprimento, altura, largura)
    potencia = calc_potencia_termometro(volume, temp_desejada, temp_ambiente)
    filtragem_min, filtragem_max = calc_filtragem(volume)
    
    print(f"Volume do aquário: {volume:.2f} litros")
    print(f"Potência do termostato necessária: {potencia:.2f} W")
    print(f"Filtragem necessária: entre {filtragem_min:.2f} e {filtragem_max:.2f} litros por hora")

main_aquario()


