from cmath import asinh as archyperbsine
from src.LinAlg import ndarray,Matrix

def asinh(x):
    if isinstance(x,ndarray):
        [rows,cols] = x.size()
        M = []
        for j in range(len(x)):
            for i in range(len(x[0])):
                M.append(archyperbsine(x[j][i]))
        return Matrix(M,rows,cols)
    else:
        return archyperbsine(x)