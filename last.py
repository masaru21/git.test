import numpy as np
from numpy.linalg import inv

x1 = 1
x2 = 3
x3 = 2
y1 = 4
y2 = 16
y3 = 9

p = np.array([[1, x1, x1**2 ], [1, x2, x2**2 ], [1, x3, x3 **2 ]])
y = np.array([[y1],[y2],[y3]])

invp = np.linalg.inv(p)
#pの逆行列

A = np.dot(invp, y)
#invpとyの行列式

print(A)
