# AUTOR: Pedro Luc Leandro
#
# DESCRIÇÃO: primeiramente, foram criadas funções (velocidade media, soma, subtração, multiplicação e divisão) para
# serem usadas na calculadora. Posteriormente, foi criada uma calculadora que realiza as operações matemáticas conforme
# as funções criadas
#
#

# DATA: 08/05
#
# VERSÃO:1.0.0
#
# LICENÇA: General Public License (GNU)
#
#
# DEFININDO AS FUNÇÕES

# FUNÇÃO DA VELOCIDADE MÉDIA
def velocidadeMedia(a, b):
    velocidade = a / b

    # CALCULANDO A VELOCIDADE MEDIA
    print(f"A distância do trajeto é: {a}Km")
    print(f"O tempo percorrido foi de: {b}h")
    print(f"A velocidade média é: {velocidade} Km/h\n")


# FUNÇÃO DA SOMA DE DOIS NÚMEROS
def soma(a, b):
    som = a + b  # CALCULANDO A SOMA
    print(f"A soma é: {a} + {b} = {som}\n")


# FUNÇÃO DA SUBTRAÇÃO
def subtracao(a, b):
    sub = a - b  # CALCULANDO A SUBTRAÇÃO
    print(f"A subtração é: {a} - {b} = {sub}\n")


# FUNÇÃO DE MULTIPLICAÇÃO
def multiplicacao(a, b):
    mult = a * b
    # CALCULANDO A MULTIPLICAÇÃO
    print(f"A multiplicação é: {a} x {b} = {mult}\n")


# FUNÇÃO DE DIVISÃO
def divisao(a, b):
    div = a / b  # CALCULANDO A DIVISÃO
    print(f"A divisão é: {a} / {b} = {div:.2f}\n")


def linha():
    print("~" * 40)


###############################################################################

# CRIANDO A CALCULADORA
linha()
print("ESCOLHA A OPERAÇÃO MATEMÁTICA DESEJADA")
linha()

print("SOMA   SUBTRAÇÃO   DIVISÃO   MULTIPLICAÇÃO   VELOCIDADE MEDIA")
escolha = input("Escolha a operação matemática desejada: ").upper()

# Definindo a acão para cada operação matemática escolhida


if escolha == "SOMA":
    print('\nVOCÊ ESCOLHEU A OPERAÇÃO "SOMA"')
    a = int(input("\nDigite o valor do primeiro número:\n"))
    b = int(input("Digite o valor do segundo número:\n"))
    soma(a, b)

if escolha == "SUBTRAÇÃO":
    print('\nVOCÊ ESCOLHEU A OPERAÇÃO "SUBTRAÇÃO"')
    a = int(input("\nDigite o valor do primeiro número:\n"))
    b = int(input("Digite o valor do segundo número:\n"))
    subtracao(a, b)

if escolha == "MULTIPLICAÇÃO":
    print('\nVOCÊ ESCOLHEU A OPERAÇÃO "MULTIPLICAÇÃO"')
    a = int(input("\nDigite o valor do primeiro número:\n"))
    b = int(input("Digite o valor do segundo número:\n"))
    multiplicacao(a, b)

if escolha == "DIVISÃO":
    print('\nVOCÊ ESCOLHEU A OPERAÇÃO "DIVISÃO"')
    a = int(input("\nDigite o valor do primeiro número:\n"))
    b = int(input("Digite o valor do segundo número:\n"))
    divisao(a, b)

if escolha == "VELOCIDADE MEDIA":
    print('\nVOCÊ ESCOLHEU A OPERAÇÃO "VELOCIDADE MEDIA"')
    a = int(input("\nQual a distância percorrida: "))
    b = int(input("Duração do trajeto:\n"))
    velocidadeMedia(a, b)
