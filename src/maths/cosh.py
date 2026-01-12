from cmath import cosh as hyperbcos
from src.LinAlg.ndarray import ndarray,Matrix

def cosh(x):
    if isinstance(x,ndarray):
        [rows, cols] = x.size
        M = []
        for j in range(rows):
            for i in range(cols):
                M.append(hyperbcos(x[j,i]).real)
        return Matrix(M,size=x.size)
    else:
        return hyperbcos(x).real
