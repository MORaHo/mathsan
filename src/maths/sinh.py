from cmath import sinh as hyperbsine
from src.LinAlg.ndarray import ndarray,Matrix

def sinh(x):
    if isinstance(x,ndarray):
        [rows, cols] = x.size
        M = []
        for j in range(rows):
            for i in range(cols):
                M.append(hyperbsine(x[j,i]).real)
        return Matrix(M,size=x.size)
    else:
        return hyperbsine(x).real
