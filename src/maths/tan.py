from cmath import tan as tangent
from src.LinAlg.ndarray import ndarray,Matrix

def tan(x):
    if isinstance(x,ndarray):
        [rows, cols] = x.size
        M = []
        for j in range(rows):
            for i in range(cols):
                M.append(tangent(x[j,i]).real)
        return Matrix(M,size=x.size)
    else:
        return tangent(x).real
