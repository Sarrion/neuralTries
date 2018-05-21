#_NEURAL_NETWORK_FORWARD_EXPRESSION____________________________________________

import sympy as sp
x, y, z, a, f = sp.symbols('x y z a f')
inp1, inp2, inp3, inp4 = sp.symbols('inp1 inp2 inp3 inp4')
i1, i2, i3, i4 = sp.symbols('i1 i2 i3 i4')


 #_input_______________________________________
input = sp.Matrix(1,4,[inp1, inp2, inp3, inp4])
#______________________________________________


 #_Weights_definitions______________________
''' SECOND WAY TO DEFINE WEIGHTS
    #_symbol_generation______________________
for i in range(1,5):
    for j in range(1,5):
        x = 'w1' + str(i) + str(j)
        y = 'symbols("w_1" + str(i) + str(j))'
        exec("%s = %s" % (x, y))
#____________________________________________
        
    #_matrix_symbol_asignations______________    
W_l1tol2 = ((4,4))
for i in range(0,4):
    for j in range(0,4):
        x = 'w1' + str(i+1) + str(j+1)
        exec("%s = %s" % (W_l1tol2[i,j], x))
#____________________________________________
'''
 
W_l1tol2 = sp.MatrixSymbol('l1t2', 4, 4) 
W_l2tol3 = sp.MatrixSymbol('l2t3', 4, 4)
W_l3tol4 = sp.MatrixSymbol('l3t4', 4, 2)
W_l4tol5 = sp.MatrixSymbol('l4t5', 2, 1)
#___________________________________________


 #_function_definition__
f = 1 / (1 + sp.exp(-x))
#_______________________


 #_outputs____________________________________________________________________
o_l1 = sp.Matrix(1,4,[f.subs(x,input[0]), f.subs(x,input[1]),
                      f.subs(x,input[2]), f.subs(x,input[3])])
o_l2 = sp.Matrix([[f.subs(x, o_l1 * sp.Matrix(W_l1tol2[:,0])),
               f.subs(x, o_l1 * sp.Matrix(W_l1tol2[:,1])),
               f.subs(x, o_l1 * sp.Matrix(W_l1tol2[:,2])),
               f.subs(x, o_l1 * sp.Matrix(W_l1tol2[:,3]))]])    
o_l3 = sp.Matrix([[f.subs(x, o_l2 * sp.Matrix(W_l2tol3[:,0])),
               f.subs(x, o_l2 * sp.Matrix(W_l2tol3[:,1])),
               f.subs(x, o_l2 * sp.Matrix(W_l2tol3[:,2])),
               f.subs(x, o_l2 * sp.Matrix(W_l2tol3[:,3]))]])
o_l4 = sp.Matrix([[f.subs(x, o_l3 * sp.Matrix(W_l3tol4[:,0])),
               f.subs(x, o_l3 * sp.Matrix(W_l3tol4[:,1]))]])
o_l5 = sp.Matrix([[f.subs(x, o_l4 * sp.Matrix(W_l4tol5[:,0]))]])
#_____________________________________________________________________________