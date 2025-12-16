from cmath import atanh as archyperbtan
from src.LinAlg import ndarray,Matrix

def atanh(x):
    if isinstance(x,ndarray):
        [rows,cols] = x.size()
        M = []
        for j in range(len(x)):
            for i in range(len(x[0])):
                M.append(archyperbtan(x[j][i]))
        return Matrix(M,rows,cols)
    else:
        return archyperbtan(x)