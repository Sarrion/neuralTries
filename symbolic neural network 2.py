#_NEURAL_NETWORK_FORWARD_EXPRESSION____________________________________________

import sympy as sp
import numpy as np
x, y, z, a, f = sp.symbols('x y z a f')
inp1, inp2, inp3, inp4 = sp.symbols('inp1 inp2 inp3 inp4')
i1, i2, i3, i4 = sp.symbols('i1 i2 i3 i4')


 #_input_______________________________________
input = sp.Matrix(1,4,[inp1, inp2, inp3, inp4])
#______________________________________________


 #_Weights_definitions________________________________________________________
   #_weights_between_layers_1_and_2_______________________________________
W_l1tol2 = []
index = 1
for i in range(1,5):
    for j in range(1,5):
        string = 'w1'+str(i)+str(j)+' = sp.symbols("w1'+str(i)+str(j)+'")'
        exec(string)
        exec('W_l1tol2.append(w1' + str(i) + str(j) + ')')
W_l1tol2 = np.array(W_l1tol2)
W_l1tol2 = W_l1tol2.reshape((4,4))
W_l1tol2 = np.matrix(W_l1tol2)
   #_weights_between_layers_2_and_3_______________________________________
W_l2tol3 = []
index = 1
for i in range(1,5):
    for j in range(1,5):
        string = 'w2'+str(i)+str(j)+' = sp.symbols("w2'+str(i)+str(j)+'")'
        exec(string)
        exec('W_l2tol3.append(w2' + str(i) + str(j) + ')')
W_l2tol3 = np.array(W_l2tol3)
W_l2tol3 = W_l2tol3.reshape((4,4))
W_l2tol3 = np.matrix(W_l2tol3)
   #_weights_between_layers_3_and_4_______________________________________
W_l3tol4 = []
index = 1
for i in range(1,5):
    for j in range(1,3):
        string = 'w3'+str(i)+str(j)+' = sp.symbols("w3'+str(i)+str(j)+'")'
        exec(string)
        exec('W_l3tol4.append(w3' + str(i) + str(j) + ')')
W_l3tol4 = np.array(W_l3tol4)
W_l3tol4 = W_l3tol4.reshape((4,2))
W_l3tol4 = np.matrix(W_l3tol4)
   #_weights_between_layers_4_and_5_______________________________________
W_l4tol5 = []
index = 1
for i in range(1,3):
    for j in range(1,2):
        string = 'w4'+str(i)+str(j)+' = sp.symbols("w4'+str(i)+str(j)+'")'
        exec(string)
        exec('W_l4tol5 .append(w4' + str(i) + str(j) + ')')
W_l4tol5 = np.array(W_l4tol5)
W_l4tol5 = W_l4tol5 .reshape((2,1))
W_l4tol5 = np.matrix(W_l4tol5 )
#_____________________________________________________________________________


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