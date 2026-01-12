from math import ceil as ceiling
from src.LinAlg.ndarray import ndarray,Matrix

def ceil(x):
    if isinstance(x,ndarray):
        [rows, cols] = x.size
        M = []
        for j in range(rows):
            for i in range(cols):
                M.append(ceiling(x[j,i]))
        return Matrix(M,size=x.size)
    else:
        return ceiling(x)
