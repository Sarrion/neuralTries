import sympy as sp


neuronsByLayer = [4,4,4,2,1]
W = []
for k in range(len(neuronsByLayer) - 1):
    auxLis = []
    for i in range(neuronsByLayer[k]):
        for j in range(neuronsByLayer[k + 1]):
            exec('w' + str(k + 1) + str(i + 1) + str(j + 1) +
                 ' = sp.symbols("w' + str(k + 1) + str(i + 1) + 
                 str(j + 1) + '")')
            exec('auxLis.append(w' + str(k + 1) + str(i + 1) +
                                str(j + 1) + ')')
    W.append(sp.Array(auxLis).reshape(neuronsByLayer[k],
             neuronsByLayer[k + 1]))



