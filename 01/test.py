import numpy as np


k=2*np.identity(2)+[[1,0],[2,3]]
k = np.linalg.inv(k)
print(k)