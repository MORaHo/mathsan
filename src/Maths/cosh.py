from cmath import cosh as hyperbcos
from src.LinAlg import ndarray,Matrix

def cosh(x):
    if isinstance(x,ndarray):
        [rows,cols] = x.size()
        M = []
        for j in range(len(x)):
            for i in range(len(x[0])):
                M.append(hyperbcos(x[j][i]))
        return Matrix(M,rows,cols)
    else:
        return hyperbcos(x)