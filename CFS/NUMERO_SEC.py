# IMPORTS
from random import randint

# PROJETO
# gerar número aleatório
numSecreto = randint(1, 10)

# decidir o nivel do jogo
# nivel 1
dificuldade = int(input("DIGITE A DIFICULDADE DE 1 A 3: "))

# momento em que o jogador define a dificuldade 1 - 10 tentativas
totalDePontos = 1000  # o total de pontos para o jogador
if dificuldade == 1:
    print("\nVOCÊ ESCOLHEU O NIVEL 1\n")
    tentativas = (range(1, 11))  # definindo o número de tentativas

    print(f">>> Você está com {totalDePontos} pontos <<<<")

if dificuldade == 2:
    print("\nVOCÊ ESCOLHEU O NIVEL 2")
    tentativas = (range(1, 6))  # definindo o número de tentativas

if dificuldade == 3:
    print("\nVOCÊ ESCOLHEU O NIVEL 3")
    tentativas = (range(1, 4))  # definindo o número de tentativas

# momento que determina o número de tentativas de cada dificuldade
for tentativa in tentativas:
    print(f"A sua tentativa é a {tentativa}º")
    numDigitado = int(input("Digite um número para adivinhar o número secreto: "))

    # definindo se o número digitado é igual ao número secreto
    if numDigitado == numSecreto:
        print(f"Parabéns você acertou o número secreto que é: {numSecreto}")
        break  # aplicando o break com intuito de para o código, impedindo que ele continue realizando o else

    # definindo se o número digitado é diferente do número secreto
    else:
        print(f"\nERRO – Tente novamente, o numero secreto não é: {numDigitado}")
        if numDigitado > numSecreto:
            print("o numero digitado é maior do que o número secreto\n")
        elif numDigitado < numSecreto:
            print("o numero digitado é menor do que o número secreto\n")

        if dificuldade == 1:
            totalDePontos -= 100

        if dificuldade == 2:
            totalDePontos -= 200

        elif dificuldade == 3:
            if tentativa > 2:
                totalDePontos -= 334

            if tentativa < 3:
                totalDePontos -= 333

        print(f"O seu total de pontos é: {totalDePontos}")

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= \n")

# Definindo as mensagens caso o jogador erre ou acerte o número secreto ao final das três tentativas
if numDigitado != numSecreto:
    print(">>>>>>>>>Fim do jogo. Você errou todas as tentativas<<<<<<<<<")
else:
    print(">>>>>>>>>PARABÉNS!!! VOCÊ ACERTOU O NÚMERO SECRETO<<<<<<<<<")
