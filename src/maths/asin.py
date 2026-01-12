from cmath import asin as arcsine
from src.LinAlg.ndarray import ndarray,Matrix

def asin(x):
    if isinstance(x,ndarray):
        [rows, cols] = x.size
        M = []
        for j in range(rows):
            for i in range(cols):
                M.append(arcsine(x[j,i]).real)
        return Matrix(M,size=x.size)
    else:
        return arcsine(x).real
