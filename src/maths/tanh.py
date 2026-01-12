from cmath import tanh as hyperbtan
from src.LinAlg.ndarray import ndarray,Matrix

def tanh(x):
    if isinstance(x,ndarray):
        [rows, cols] = x.size
        M = []
        for j in range(rows):
            for i in range(cols):
                M.append(hyperbtan(x[j,i]).real)
        return Matrix(M,size=x.size)
    else:
        return hyperbtan(x).real
