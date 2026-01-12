from cmath import asinh as archyperbsine
from src.LinAlg.ndarray import ndarray,Matrix

def asinh(x):
    if isinstance(x,ndarray):
        [rows, cols] = x.size
        M = []
        for j in range(rows):
            for i in range(cols):
                M.append(archyperbsine(x[j,i]).real)
        return Matrix(M,size=x.size)
    else:
        return archyperbsine(x).real
