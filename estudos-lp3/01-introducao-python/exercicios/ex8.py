def contar_palavras(texto):

    contagem_palavras = {}
    
    palavras = texto.lower().split()
    
    for palavra in palavras:
        palavra = ''.join(char for char in palavra if char.isalnum())
        if palavra:
            if palavra in contagem_palavras:
                contagem_palavras[palavra] += 1
            else:
                contagem_palavras[palavra] = 1
                
    return contagem_palavras


texto = input("Por favor, insira um texto: ")
    
contagem = contar_palavras(texto)
    
print("\nAqui está a contagem de palavras:")
for palavra, quantidade in contagem.items():
    print(f"{palavra}: {quantidade}")