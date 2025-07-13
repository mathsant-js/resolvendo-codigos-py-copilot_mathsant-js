numero = input("Digite um número: ")

if numero.isdigit():
    numero = int(numero)
    if numero % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")
elif numero == "":
    print("Por favor, digite um número válido.")
else:
    print("Entrada inválida. Certifique-se de digitar um número inteiro.")