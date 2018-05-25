import sympy as sp
from sympy import tensorcontraction as tenCon
from sympy import tensorproduct as tenProd
inp1, inp2, inp3, inp4, f = sp.symbols('inp1 inp2 inp3 inp4 f')
    

 #_Weights_definitions_________________________________________________________
neuronsByLayer = [5,10,10,5,1]
W = []
for k in range(len(neuronsByLayer) - 1):
    auxLis = []
    for i in range(neuronsByLayer[k]):
        for j in range(neuronsByLayer[k + 1]):
            exec('w' + str(k+1) + str(i+1) + str(j+1) +
                 ' = sp.symbols("w' + str(k+1) + str(i+1) + str(j+1) + '")')
            exec('auxLis.append(w' + str(k+1) + str(i+1) + str(j+1) + ')')
    W.append(sp.Array(auxLis).reshape(neuronsByLayer[k],
             neuronsByLayer[k + 1]))
#______________________________________________________________________________


 #_input___________________________________________________________
input = []
for i in range(neuronsByLayer[0]):
    exec('inp' + str(i+1) + ' = sp.symbols("inp' + str(i+1) + '")')
    exec('input.append(inp' + str(i+1) + ')')
#__________________________________________________________________
    
    
 #_function_definition_and_input__________
f = lambda x: 1 / (1 + sp.exp(-x))
#_________________________________________


 #_Outputs_____________________________________________________________________
o = [sp.Array(input).applyfunc(f)]
for i in range(1, len(neuronsByLayer)):
    o.append(tenCon(tenProd(o[i-1], W[i-1]).applyfunc(f), (0,1)))
#______________________________________________________________________________