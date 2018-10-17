import numpy as np


#_function_____________________
def f(x):
    return 1 / (1 + np.exp(-x))
#______________________________


 #_weights_____________________________________________________________________
def net(neurByLayer):
    w = []
    for k in range(len(neurByLayer) - 1):
        w.append(np.random.random(neurByLayer[k] * neurByLayer[k + 1]).reshape(
                neurByLayer[k], neurByLayer[k + 1]))
    return w
neurByLayer = [40,40,10,20,1]
w = net(neurByLayer)
#______________________________________________________________________________


 #_input______________________________
inpt = np.array(range(neurByLayer[0]))
#_____________________________________


 #_output__________________________________
out_2 = [f(inpt)]
for i in range(len(neurByLayer)-1):
    out_2.append(f(np.dot(out_2[i], w[i])))
#__________________________________________
