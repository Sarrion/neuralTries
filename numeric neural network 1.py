import numpy as np


 #_input____________________
inp = np.array([1, 2, 3, 4])
#___________________________


#_function____________________
def f(x):
    return 1 / (1 + np.exp(x))
#_____________________________


 #_weights_____________________________________________________________________
def net(neurByLayer):
    w = []
    for k in range(len(neurByLayer) - 1):
        w.append(np.random.random(neurByLayer[k] * neurByLayer[k + 1]).reshape(
                neurByLayer[k], neurByLayer[k + 1]))
    return w
w = net([4,4,4,2,1])
#______________________________________________________________________________


 #_output__________________
out = inp
for i in range(4):
    out = f(out)
    out = np.dot(out, w[i])
out = f(out)
#__________________________