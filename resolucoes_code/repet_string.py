# Recebe o texto que será repetido.
string = input("Digite uma string: ")

# Recebe quantas vezes o texto deve ser repetido e converte a entrada para inteiro.
numero = int(input("Digite um número inteiro: "))

# Repete o texto e separa cada cópia com uma quebra de linha.
print("\n".join([string] * numero))

