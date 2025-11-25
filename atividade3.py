# Operações Matemáticas Simples

# Solicitando entrada de dados
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Realizando operações matemáticas básicas
soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2 if numero2 != 0 else "Erro: divisão por zero"

# Exibindo resultados
print(f"\nResultados:")
print(f"Adição: {numero1} + {numero2} = {soma}")
print(f"Subtração: {numero1} - {numero2} = {subtracao}")
print(f"Multiplicação: {numero1} * {numero2} = {multiplicacao}")
print(f"Divisão: {numero1} / {numero2} = {divisao}")