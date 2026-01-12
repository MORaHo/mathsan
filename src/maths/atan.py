from cmath import atan as arctangent
from src.LinAlg.ndarray import ndarray,Matrix

def atan(x):
    if isinstance(x,ndarray):
        [rows, cols] = x.size
        M = []
        for j in range(rows):
            for i in range(cols):
                M.append(arctangent(x[j,i]).real)
        return Matrix(M,size=x.size)
    else:
        return arctangent(x).real
