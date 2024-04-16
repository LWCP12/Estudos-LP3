def contar_vogais_e_consoantes(frase):
    vogais = "aeiouAEIOU"
    consoantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

    num_vogais = 0
    num_consoantes = 0

    for char in frase:
        if char in vogais:
            num_vogais += 1
        elif char in consoantes:
            num_consoantes +=1
    
    return num_vogais, num_consoantes

frase = input('Digite a frase a ser analisada:\n')

num_vogais, num_consoantes = contar_vogais_e_consoantes(frase)

print(f"Na frase, existem {num_vogais} vogais e {num_consoantes} consoantes.")
