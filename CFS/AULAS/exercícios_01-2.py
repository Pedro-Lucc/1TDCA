# IMPORTS
import random


# DEFININDO A FUNÇÃO
def exibTentativas(tAtual):
    print("Você está na tentativa", tAtual)


# Definindo as variaveis de tentativas
tentativaAtual = 1
numTentativa = 3

# PROJETO
# gerar número aleatório
numSecreto = random.randint(0, 10)

# Primeira tentativa (1/3)
exibTentativas(tentativaAtual)

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

# Definindo a quantidade de tentativas (2 e 3)
while numDigitado != numSecreto:
    if tentativaAtual > 2:
        break
    tentativaAtual += 1
    exibTentativas(tentativaAtual)
    numDigitado = int(input("Insira um novo número: "))

# Definindo se o número digitado é o correto
    if numDigitado == numSecreto:
        print(f"Parabéns você acertou o número secreto que é: {numSecreto}")
    # Definindo se o número digitado é incorreto
    else:
        print(f"ERRO – Tente novamente, o numero secreto não é {numDigitado}")
        # Dando a dica para saber se o número secreto é maior ou menor
        if numDigitado > numSecreto:
            print("O número secreto é menor do que o número digitado")
        else:
            print("O número secreto é maior do que o número digitado")

# Fazer com que o programa pule uma linha
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= \n")
# Definindo as mensagens caso o jogador erre ou acerte o número secreto ao final das três tentativas
if numDigitado != numSecreto:
    print(">>>>>>>>>Fim do jogo. Você errou todas as tentativas<<<<<<<<<")
else:
    print(">>>>>>>>>PARABÉNS!!!  VOCÊ ACERTOU O NÚMERO SECRETO<<<<<<<<<")