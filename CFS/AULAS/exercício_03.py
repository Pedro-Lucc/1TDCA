# DECLARANDO LISTAS
lista = [10, -2, 4, 8, 100, 44, -19, 2, 3, 2, -90, 11, -33, 10, 67, 15]
numPares = []
numNegativos = []
numPositivos = []
numRepetidos = []

# DECLARANDO O MAIOR NÚMERO DA LISTA
print(max(lista))

# DECLARANDO O MENOR NÚMERO DA LISTA
print(min(lista))

# IMPRIMINDO OS NÚMEROS PARES
for par in lista:
    if par % 2 == 0:
        numPares.append(par)
print(numPares)

# IMPRIMINDO O NÚMERO DE OCORRÊNCIA DO PRIMEIRO ELEMENTO DA LISTA
print(lista[0])

# IMPRIMINDO A MEDIA DOS ELEMENTOS DA LISTA
media = sum(lista) / len(lista)
print(media)

# IMPRIMINDO A SOMA DOS ELEMENTOS NEGATIVOS
for numNeg in lista:
    if numNeg < 0:
        numNegativos.append(numNeg)
print(sum(numNegativos))

# IMPRIMINDO A SOMA DOS ELEMENTOS POSITIVOS
for numPosi in lista:
    if numPosi > 0:
        numPositivos.append(numPosi)
print(sum(numPositivos))


# IMPRIMINDO ELEMENTOS REPETIDOS
for numRep in lista:
    if lista.count(numRep) > 1:
        numRepetidos.append(numRep)
numRepetidos = list(dict.fromkeys(numRepetidos))
numRepetidos.sort()
print(numRepetidos)
