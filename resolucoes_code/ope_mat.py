# Lê os dois valores digitados e converte cada um para número decimal.
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Solicita o símbolo da operação que será executada.
operacao = input("Qual operação deseja realizar? (+, -, *, /): ")

# Executa apenas a operação escolhida pelo usuário.
if operacao == "+":
    resultado = numero1 + numero2
elif operacao == "-":
    # abs() mantém a diferença entre os números sempre positiva.
    resultado = abs(numero1 - numero2)
elif operacao == "*":
    resultado = numero1 * numero2
elif operacao == "/":
    # Impede a divisão por zero, que não é permitida.
    if numero2 == 0:
        print("Não é possível dividir por zero.")
        # None indica que não há um resultado válido para exibir.
        resultado = None
    else:
        resultado = numero1 / numero2
else:
    print("Operação inválida.")
    # None indica que o símbolo informado não corresponde a uma operação aceita.
    resultado = None

# Exibe o resultado somente quando uma operação válida foi concluída.
if resultado is not None:
    print("Resultado:", resultado)
