import sympy as sp
from sympy import tensorcontraction as tenCon
from sympy import tensorproduct as tenProd
inp1, inp2, inp3, inp4, f = sp.symbols('inp1 inp2 inp3 inp4 f')


 #_Weights_definitions_________________________________________________________
def weights(FromLayer, outputNeurons, inputNeurons):
    W = []
    for i in range(1,outputNeurons + 1):
        for j in range(1,inputNeurons + 1):
            exec('w' + str(FromLayer) + str(i) + str(j) +
            ' = sp.symbols("w' + str(FromLayer) + str(i) + str(j) + '")')
            exec('W.append(w' + str(FromLayer) + str(i) + str(j) + ')')
    W = sp.Array(W)
    W = W.reshape(outputNeurons, inputNeurons)
    return(W)
   #_from_layer_1_to_2_____
W_l1tol2 = weights(1, 4, 4)
   #_from_layer_2_to_3_____
W_l2tol3 = weights(2, 4, 4)
   #_from_layer_3_to_4_____
W_l3tol4 = weights(3, 4, 2)
   #_from_layer_4_to_5_____
W_l4tol5 = weights(4, 2, 1)
#______________________________________________________________________________


 #_function_definition_and_input__________
f = lambda x: 1 / (1 + sp.exp(-x))
input = sp.Array([inp1, inp2, inp3, inp4])
#_________________________________________


 #_Outputs_____________________________________________________________________
o_l1 = [f(input[0]), f(input[1]), f(input[2]), f(input[3])]
o_l2 = tenCon(tenProd(o_l1, W_l1tol2).applyfunc(f), (0,1))
o_l3 = tenCon(tenProd(o_l2, W_l2tol3).applyfunc(f), (0,1))
o_l4 = tenCon(tenProd(o_l3, W_l3tol4).applyfunc(f), (0,1))
o_l5 = tenCon(tenProd(o_l4, W_l4tol5).applyfunc(f), (0,1))
#______________________________________________________________________________