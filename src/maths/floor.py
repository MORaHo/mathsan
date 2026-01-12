from math import floor as flooring
from src.LinAlg.ndarray import ndarray,Matrix

def floor(x):
    if isinstance(x,ndarray):
        [rows, cols] = x.size
        M = []
        for j in range(rows):
            for i in range(cols):
                M.append(flooring(x[j,i]))
        return Matrix(M,size=x.size)
    else:
        return flooring(x)
