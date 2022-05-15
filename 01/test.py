import numpy as np


X = np.arange(-20, 35, 0.1) 
Y = np.arange(-20, 35, 0.1)
[XX, YY] = np.meshgrid(X, Y)


print(XX.shape)
print(X.shape)