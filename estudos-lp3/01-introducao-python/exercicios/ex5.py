def verificar_palindromo(texto):
    texto_limpo = ''.join(char.lower() for char in texto if char.isalnum())
    return texto_limpo == texto_limpo[::-1]

def main():
    texto = input("Digite uma palavra ou frase: ")
    
    if verificar_palindromo(texto):
        print(f'"{texto}" é um palíndromo.')
    else:
        print(f'"{texto}" não é um palíndromo.')

main()
