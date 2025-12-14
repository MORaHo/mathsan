from math import sqrt as sqroot
from src.LinAlg import ndarray,Matrix

def sqrt(x):
    if isinstance(x,ndarray):
        [rows,cols] = x.size()
        M = []
        for j in range(len(x)):
            for i in range(len(x[0])):
                M.append((sqroot(x[j][i])))
        return Matrix(M,rows,cols)
    else:
        return sqroot(x)