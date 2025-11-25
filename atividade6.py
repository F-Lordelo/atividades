def is_palindrome(word):
    # Remove espaços e converte para minúsculas
    cleaned_word = word.replace(" ", "").lower()
    # Inverte a palavra
    reversed_word = cleaned_word[::-1]
    # Compara a palavra original com a invertida
    return cleaned_word == reversed_word

# Testando a função
word = input("Digite uma palavra ou frase: ")
if is_palindrome(word):
    print(f'"{word}" é um palíndromo!')
else:
    print(f'"{word}" não é um palíndromo.')