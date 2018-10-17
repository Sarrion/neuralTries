import sympy as sp
inp1, inp2, inp3, inp4, f = sp.symbols('inp1 inp2 inp3 inp4 f')


 #_Weights_definitions_________________________________________________________
def weights(FromLayer, outputNeurons,inputNeurons):
    W = []
    for i in range(1,outputNeurons + 1):
        for j in range(1,inputNeurons + 1):
            exec('w' + str(FromLayer) + str(i) + str(j) +
            ' = sp.symbols("w' + str(FromLayer) + str(i) + str(j) + '")')
            exec('W.append(w' + str(FromLayer) + str(i) + str(j) + ')')
    W = sp.Array(W)
    W = W.reshape(outputNeurons, inputNeurons)
    return(W)
   #_weights_between_layers_1_and_2____
W_l1tol2 = weights(1, 4, 4)
   #_weights_between_layers_2_and_3____
W_l2tol3 = weights(2, 4, 4)
   #_weights_between_layers_3_and_4____
W_l3tol4 = weights(3, 4, 2)
   #_weights_between_layers_4_and_5____
W_l4tol5 = weights(4, 2, 1)
#______________________________________________________________________________


 #_function_definition_and_input______________
f = lambda x: 1 / (1 + sp.exp(-x))
input = sp.Array([inp1, inp2, inp3, inp4])
#_____________________________________________


 #_Outputs_____________________________________________________________________
o_l1 = [f(input[0]), f(input[1]), f(input[2]), f(input[3])]
o_l2 = sp.tensorcontraction(sp.tensorproduct([o_l1], W_l1tol2)[0,:,:,:].applyfunc(f), (0,1))
o_l3 = sp.tensorcontraction(sp.tensorproduct([o_l2], W_l2tol3)[0,:,:,:].applyfunc(f), (0,1))
o_l4 = sp.tensorcontraction(sp.tensorproduct([o_l3], W_l3tol4)[0,:,:,:].applyfunc(f), (0,1))
o_l5 = sp.tensorcontraction(sp.tensorproduct([o_l4], W_l4tol5)[0,:,:,:].applyfunc(f), (0,1))
#______________________________________________________________________________