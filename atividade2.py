# atividade2.py
# Programa: Repetindo Textos
# Pede uma string e um inteiro e exibe a string repetida esse número de vezes.

def main():
    texto = input("Digite uma string: ")
    while True:
        n_str = input("Digite um número inteiro (>= 0): ")
        try:
            n = int(n_str)
            if n < 0:
                print("Por favor, informe um inteiro não-negativo.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Digite um número inteiro válido.")

    resultado = texto * n
    print("\nResultado:")
    print(resultado)

if __name__ == "__main__":
    main()