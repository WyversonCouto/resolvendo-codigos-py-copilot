# Solicita ao usuário um número inteiro.
numero = int(input("Digite um número inteiro: "))

# Verifica se o número é divisível por 2, sem deixar resto.
if numero % 2 == 0:
    # Exibe a mensagem para números pares.
    print("O número é par.")
else:
    # Exibe a mensagem para números ímpares.
    print("O número é ímpar.")
    