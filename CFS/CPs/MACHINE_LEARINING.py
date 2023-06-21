from sklearn import tree

laranja = 0
maca = 1
lisa = 1
irregular = 0

pomar = [[150, lisa], [130, lisa], [160, irregular], [180, irregular]]
resultado = [maca, maca, laranja, laranja]

classificador = tree.DecisionTreeClassifier()
# O fit serve para construir uma árvore de decisão, baseado em X e Y
classificador = classificador.fit(pomar, resultado)

peso = input('Por favor, entre com o peso da fruta: ')
superficie = input('Por favor, entre com o tipo de superficie (0) irregular (1) lisa: ')

# O predict serve para pré-dizer o resultado comparando os valores de X e Y
resultadoUsuario = classificador.predict([[peso, superficie]])
print(resultadoUsuario)

if resultadoUsuario == 1:
    print('É UMA MAÇÃ')
else:
    print('É UMA MAÇÃ')





