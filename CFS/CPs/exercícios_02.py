# IMPORTS
from random import randint

# PROJETO
# gerar número aleatório
numSecreto = randint(1, 10)

# decidir o nivel do jogo
# nivel 1
dificuldade = int(input("DIGITE A DIFICULDADE DE 1 A 3: "))


# momento em que o jogador define a dificuldade 1 - 10 tentativas
if dificuldade == 1:
    print("\nVOCÊ ESCOLHEU O NIVEL 1")
    tentativaN1 = (range(1, 11))

if dificuldade == 2:
    print("\nVOCÊ ESCOLHEU O NIVEL 2")
    tentativaN1 = (range(1, 6))

if dificuldade == 3:
    print("\nVOCÊ ESCOLHEU O NIVEL 3")
    tentativaN1 = (range(1, 4))



for tentativa in tentativaN1:
    print(f"você está na tentativa {tentativa}")
    numDigitado = int(input("Digite um número para adivinhar o número secreto: "))
    if numDigitado == numSecreto:
        print(f"Parabéns você acertou o número secreto que é: {numSecreto}")
        break
    else:
        print(f"\nERRO – Tente novamente, o numero secreto não é: {numDigitado}")
        if numDigitado > numSecreto:
            print("o numero digitado é maior do que o número secreto\n")
        elif numDigitado < numSecreto:
            print("o numero digitado é menor do que o número secreto\n")

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= \n")
# Definindo as mensagens caso o jogador erre ou acerte o número secreto ao final das três tentativas
if numDigitado != numSecreto:
    print(">>>>>>>>>Fim do jogo. Você errou todas as tentativas<<<<<<<<<")
else:
    print(">>>>>>>>>PARABÉNS!!! VOCÊ ACERTOU O NÚMERO SECRETO<<<<<<<<<")