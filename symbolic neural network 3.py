import sympy as sp
inp1, inp2, inp3, inp4, f = sp.symbols('inp1 inp2 inp3 inp4 f')


 #_Weights_definitions_________________________________________________________
   #_weights_between_layers_1_and_2_______________________________________
W_l1tol2 = []
index = 1
for i in range(1,5):
    for j in range(1,5):
        string = 'w1'+str(i)+str(j)+' = sp.symbols("w1'+str(i)+str(j)+'")'
        exec(string)
        exec('W_l1tol2.append(w1' + str(i) + str(j) + ')')
W_l1tol2 = sp.Array(W_l1tol2)
W_l1tol2 = W_l1tol2.reshape(4,4)
   #_weights_between_layers_2_and_3_______________________________________
W_l2tol3 = []
index = 1
for i in range(1,5):
    for j in range(1,5):
        string = 'w2'+str(i)+str(j)+' = sp.symbols("w2'+str(i)+str(j)+'")'
        exec(string)
        exec('W_l2tol3.append(w2' + str(i) + str(j) + ')')
W_l2tol3 = sp.Array(W_l2tol3)
W_l2tol3 = W_l2tol3.reshape(4,4)
   #_weights_between_layers_3_and_4_______________________________________
W_l3tol4 = []
index = 1
for i in range(1,5):
    for j in range(1,3):
        string = 'w3'+str(i)+str(j)+' = sp.symbols("w3'+str(i)+str(j)+'")'
        exec(string)
        exec('W_l3tol4.append(w3' + str(i) + str(j) + ')')
W_l3tol4 = sp.Array(W_l3tol4)
W_l3tol4 = W_l3tol4.reshape(4,2)
   #_weights_between_layers_4_and_5_______________________________________
W_l4tol5 = []
index = 1
for i in range(1,3):
    for j in range(1,2):
        string = 'w4'+str(i)+str(j)+' = sp.symbols("w4'+str(i)+str(j)+'")'
        exec(string)
        exec('W_l4tol5 .append(w4' + str(i) + str(j) + ')')
W_l4tol5 = sp.Array(W_l4tol5)
W_l4tol5 = W_l4tol5 .reshape(2,1)
#______________________________________________________________________________


 #_function_definition_and_input______________
f = lambda x: 1 / (1 + sp.exp(-x))
input = sp.Array(1,4,[inp1, inp2, inp3, inp4])
#_____________________________________________


 #_Outputs_____________________________________________________________________
o_l1 = sp.Array([[f(input[0]), f(input[1]), f(input[2]), f(input[3])]])
o_l2 = sp.Array([[f(o_l1[0]*W_l1tol2[:,0][0]) +
                    f(o_l1[1]*W_l1tol2[:,0][1]) +
                     f(o_l1[2]*W_l1tol2[:,0][2]) +
                      f(o_l1[3]*W_l1tol2[:,0][3])],
                  [f(o_l1[0]*W_l1tol2[:,1][0]) +
                    f(o_l1[1]*W_l1tol2[:,1][1]) +
                     f(o_l1[2]*W_l1tol2[:,1][2]) +
                      f(o_l1[3]*W_l1tol2[:,1][3])],
                  [f(o_l1[0]*W_l1tol2[:,2][0]) +
                    f(o_l1[1]*W_l1tol2[:,2][1]) +
                     f(o_l1[2]*W_l1tol2[:,2][2]) +
                      f(o_l1[3]*W_l1tol2[:,2][3])],
                  [f(o_l1[0]*W_l1tol2[:,3][0]) +
                    f(o_l1[1]*W_l1tol2[:,3][1]) +
                     f(o_l1[2]*W_l1tol2[:,3][2]) +
                      f(o_l1[3]*W_l1tol2[:,3][3])]])
o_l3 = sp.Array([[f(o_l2[0]*W_l2tol3[:,0][0]) +
                    f(o_l2[1]*W_l2tol3[:,0][1]) +
                     f(o_l2[2]*W_l2tol3[:,0][2]) +
                      f(o_l2[3]*W_l2tol3[:,0][3])],
                  [f(o_l2[0]*W_l2tol3[:,1][0]) +
                    f(o_l2[1]*W_l2tol3[:,1][1]) +
                     f(o_l2[2]*W_l2tol3[:,1][2]) +
                      f(o_l2[3]*W_l2tol3[:,1][3])],
                  [f(o_l2[0]*W_l2tol3[:,2][0]) +
                    f(o_l2[1]*W_l2tol3[:,2][1]) +
                     f(o_l2[2]*W_l2tol3[:,2][2]) +
                      f(o_l2[3]*W_l2tol3[:,2][3])],
                  [f(o_l2[0]*W_l2tol3[:,3][0]) +
                    f(o_l2[1]*W_l2tol3[:,3][1]) +
                     f(o_l2[2]*W_l2tol3[:,3][2]) +
                      f(o_l2[3]*W_l2tol3[:,3][3])]])
o_l4 = sp.Array([[f(o_l3[0]*W_l3tol4[:,0][0]) +
                    f(o_l3[1]*W_l3tol4[:,0][1]) +
                     f(o_l3[2]*W_l3tol4[:,0][2]) +
                      f(o_l3[3]*W_l3tol4[:,0][3])],
                  [f(o_l3[0]*W_l3tol4[:,1][0]) +
                    f(o_l3[1]*W_l3tol4[:,1][1]) +
                     f(o_l3[2]*W_l3tol4[:,1][2]) +
                      f(o_l3[3]*W_l3tol4[:,1][3])]])   
o_l5 = sp.Array([[f(o_l4[0]*W_l4tol5[:,0][0]) + 
                    f(o_l4[1]*W_l4tol5[:,0][1])]])
#______________________________________________________________________________