from typing import Optional

#!/usr/bin/env python3
"""

Verifica se um número inteiro é par ou ímpar.
Conceitos usados: if/else, operador módulo (%) e tratamento de entrada.
"""

def is_even(n: int) -> bool:
    """Retorna True se n for par, False caso contrário."""
    return n % 2 == 0


def read_int(prompt: str = "Digite um número inteiro (ou 'sair' para encerrar): ") -> Optional[int]:
    """Lê um inteiro do usuário; retorna None se o usuário optar por sair."""
    while True:
        s = input(prompt).strip()
        if s.lower() in {"sair", "exit", "q"}:
            return None
        try:
            return int(s)
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro ou digite 'sair' para encerrar.")


def main() -> None:
    while True:
        n = read_int()
        if n is None:
            print("Encerrando.")
            break
        if is_even(n):
            print(f"O número {n} é par.")
        else:
            print(f"O número {n} é ímpar.")


if __name__ == "__main__":
    main()