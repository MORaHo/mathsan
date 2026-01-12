from cmath import sin as sine
from src.LinAlg.ndarray import ndarray,Matrix

def sin(x):
    if isinstance(x,ndarray):
        [rows, cols] = x.size
        M = []
        for j in range(rows):
            for i in range(cols):
                M.append(sine(x[j,i]).real)
        return Matrix(M,size=x.size)
    else:
        return sine(x).real
