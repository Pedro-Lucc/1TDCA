# AUTOR: Pedro Luc Leandro
#
# DESCRIÇÃO: este programa exibe o jogo da forca, na qual, um jogador insere várias letras para completar uma palavra,
# caso ele erre, uma tentativa será
# perdida, no total são 10, e se a palavra não for completada ao final das tentativas, o jogo será encerrado como
# derrota.
# Contudo, caso ele acerte a letra, a tentativa continuará a contar e a letra digitada corretamente aparecerá na tela.
# Se o jogador acertar todas as letras e completar a palavra no final ele vencerá.
#

# DATA: 08/05
#
# VERSÃO:1.0.0
#
# LICENÇA: General Public License (GNU)
#
#
# JOGO DA FORCA

# IMPORTANTO

import random

# definindo a palavra secreta
palavras = ["topete", "casa", "lugar", "escola", "caneta", "fone", "quadrado", "controle"]
palavras1 = random.choice(palavras)

# Definindo as variaveis de tentativas
tentativaAtual = 0
totalTentativa = 10
letrasUtilizadas = []
arrPalavraCerta = []
nAcerto = 0
nErros = 0
i = 0


# FUNÇÕES
def linha():
    print("=" * 40)


def IsAcertou():
    if '_' in str(arrPalavraCerta):
        return 0
    else:
        return 1


def mostraResult():
    s = ""
    n = 0
    while n < len(arrPalavraCerta):
        s += arrPalavraCerta[n]
        n += 1
    linha()
    print(s)
    linha()


# DECIDINDO A POSIÇÃO DA LETRA
def setPosLetraCerta(letra, nAcerto, nErros, tentativaAtual, totalTentativa):
    j = 0
    m = len(palavras1)
    tentativaAtual += 1

    # DETERMINANDO O NÚMERO DE TENTATIVAS
    while j < m:
        if tentativaAtual < totalTentativa:
            tentativaAtual += 1

        # DEFININDO SE A LETRA DIGITADA É CORREPONDENTE À PALAVRA EM QUESTÃO
        letraDaVez = palavras1[j:(j + 1)]
        if letraDaVez == letra:
            nAcerto += 1
            arrPalavraCerta[j] = letra
        else:
            nErros += 1

        j += 1


# PRINT PARA MOSTRAR SE A LETRA DIGITADA FOI PREENCHIDA
print(arrPalavraCerta)

# WHILE CRIADO PARA SABER O TAMANHO DA PALAVRA E ADICIONAR AS POSIÇÕES DAS LETRAS
while i < len(palavras1):
    arrPalavraCerta.append("_")
    i += 1


# INICIANDO O PROGRAMA DO JOGO DA FORCA

def Inicia(tentativaAtual, totalTentativa):
    tentativaAtual += 1

    # IF PARA MOSTRAR AS REGRAS E O INÍCIO DO JOGO SOMENTE UMA VEZ
    if tentativaAtual == 1:
        linha()
        print("OLÁ, SEJA BEM-VINDO AO JOGO DA FORCA")
        linha()
        print("\nREGRAS DO JOGO: ")
        print(" * você deverá escolher uma letra para cada palavra")
        print(" * se você errar uma letra, o boneco ficará mais próximo de ser ENFORCADO")
        print(" * se você acertar, a letra aparecerá na tela,")
        print("   complementando assim o espaço para a formação da palavra\n")
        print("!!!!! TOME MUITOOOOO CUIDADO !!!!!\n")

    # PRIN PARA MOSTRAR EM QUAL TENTATIVA O JOGADOR ESTÁ
    print(f"totalTentativa = {totalTentativa}")
    print(f"tentativaAtual = {tentativaAtual}")
    print(f"restam {totalTentativa - tentativaAtual} tentativa(s)")

    # PRINT PARA INDICAR O COMANDO DE DIGITAÇÃO DA LETRA
    print(" * você deverá escolher uma letra para cada palavra")

    # INPUT PARA O JOGADOR DIGITAR A LETRA
    letra = input("Digite uma letra: ")
    setPosLetraCerta(letra, nAcerto, nErros, tentativaAtual, totalTentativa)
    mostraResult()

    # DELIMITANDO O TOTAL DE TENTATIVAS QUE O JOGAR TERÁ.
    if tentativaAtual != totalTentativa:
        if IsAcertou():
            print("ACERTOU")
        else:
            Inicia(tentativaAtual, totalTentativa)
    else:
        print("Tentativas esgotadas, fim do jogo")


Inicia(tentativaAtual, totalTentativa)
