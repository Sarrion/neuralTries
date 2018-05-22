import numpy as np

w = []
neurByLayer = [4, 4, 4, 2, 1]
for k in range(len(neurByLayer) - 1):
    w.append(np.random.random(neurByLayer[k] * neurByLayer[k + 1]).reshape(
            neurByLayer[k], neurByLayer[k + 1]))



