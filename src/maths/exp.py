from cmath import exp as exponential
from src.LinAlg.ndarray import ndarray,Matrix

def exp(x):
    if isinstance(x,ndarray):
        [rows, cols] = x.size
        M = []
        for j in range(rows):
            for i in range(cols):
                M.append(exponential(x[j,i]))
        return Matrix(M,size=x.size)
    else:
        return exponential(x)
