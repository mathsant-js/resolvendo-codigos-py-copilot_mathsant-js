# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

operacao = input("Digite a operação desejada (soma, subtracao, multiplicacao, divisao): ").strip().lower()

if operacao == "soma":
    resultado = num1 + num2
    print(f"A soma de {num1} e {num2} é: {resultado}")
elif operacao == "subtracao":
    resultado = num1 - num2
    print(f"A subtração de {num1} e {num2} é: {resultado}")
elif operacao == "multiplicacao":
    resultado = num1 * num2
    print(f"A multiplicação de {num1} e {num2} é: {resultado}")
elif operacao == "divisao":
    resultado = num1 / num2 if num2 != 0 else "Indefinido (divisão por zero)"
    print(f"A divisão de {num1} por {num2} é: {resultado}")
else:
    print("Operação inválida. Por favor, escolha entre soma, subtracao, multiplicacao ou divisao.")