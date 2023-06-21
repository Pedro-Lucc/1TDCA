import argparse

# Definindo um objeto para podermos passar os argumentos
parser = argparse.ArgumentParser('Calcular a área do terreno')

# Definindo os argumentos do objeto "paser" com o método add_arguments()
parser.add_argument('Largura', type=int, help='Largura do Terreno')
parser.add_argument('Comprimento', type=int, help='Comprimento do Terreno')

# Criando um objeto que irá armazenar os argumentos passados no objeto "parser"
args = parser.parse_args()


def calc_area(largura, comprimento):
    area = largura * comprimento
    return area


if __name__ == '__main__':
    print(f'a area do terreno é {calc_area(args.largura, args.comprimento)} ')
