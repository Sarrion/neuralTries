
import sympy as sp
import numpy as np
#%%

lis = []
index = 1

for i in range(1,4):
    for j in range(1,4):
        string = 'a' + str(i) + str(j) + ' = sp.symbols("a' + str(i) + str(j)  + '")'
        print(string)
        exec(string)
        exec('lis.append(a' + str(i) + str(j) + ')')
lis = np.array(lis)
lis = lis.reshape((3,3))
lis = np.matrix(lis)
