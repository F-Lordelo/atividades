# Calculando Média de Notas 📚
# Solicita três notas ao usuário e calcula a média aritmética.

def ler_nota(ordem):
    while True:
        try:
            entrada = input(f"Digite a {ordem}ª nota: ").strip()
            # aceita vírgula como separador decimal
            return float(entrada.replace(',', '.'))
        except ValueError:
            print("Entrada inválida. Informe um número (use . ou , para decimais).")

def main():
    print("Calculando a média de três notas")
    n1 = ler_nota(1)
    n2 = ler_nota(2)
    n3 = ler_nota(3)

    media = (n1 + n2 + n3) / 3  # uso de operadores aritméticos (+, /)

    print(f"\nNotas informadas: {n1:.2f}, {n2:.2f}, {n3:.2f}")
    print(f"Média: {media:.2f}")

if __name__ == "__main__":
    main()