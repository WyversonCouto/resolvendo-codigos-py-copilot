# Vamos testar se uma palavra é um palíndromo?! Uma dica é: Utilize conceitos de manipulação de strings para inverter a palavra e comparar com a original.
palavra = input("Digite uma palavra: ")

# Converte a palavra para minúsculas e remove espaços em branco.
palavra = palavra.lower().strip()

# Inverte a palavra.
palavra_invertida = palavra[::-1]

# Compara a palavra original com a invertida.
if palavra == palavra_invertida:
    print("A palavra é um palíndromo.")
else:
    print("A palavra não é um palíndromo.")
