from cmath import asin as arcsine
from src.LinAlg import ndarray,Matrix

def asin(x):
    if isinstance(x,ndarray):
        [rows,cols] = x.size()
        M = []
        for j in range(len(x)):
            for i in range(len(x[0])):
                M.append(arcsine(x[j][i]))
        return Matrix(M,rows,cols)
    else:
        return arcsine(x)