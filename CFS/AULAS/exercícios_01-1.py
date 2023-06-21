# IMPORTS
import random

# PROJETO
# gerar número aleatório
numSecreto = random.randint(0, 10)

# inserindo um chute
numDigitado = int(input("Tente descobrir o número aleatório. Digite um número: "))

# Descobrindo se o número digitado é o correto
if numDigitado == numSecreto:
    print(f"Parabéns você acertou o número secreto que é: {numSecreto}")
else:
    print(f"ERRO – Tente novamente, o numero secreto não é {numDigitado}")
    # Dando a dica para saber se o número secreto é maior ou menor
    if numDigitado > numSecreto:
        print("O número secreto é menor do que o número digitado")
    else:
        print("O número secreto é maior do que o número digitado")
