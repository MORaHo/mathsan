from math import floor as flooring
from src.LinAlg import ndarray,Matrix

def floor(x):
    if isinstance(x,ndarray):
        [rows,cols] = x.size()
        M = []
        for j in range(len(x)):
            for i in range(len(x[0])):
                M.append(flooring(x[j][i]))
        return Matrix(M,rows,cols)
    else:
        return flooring(x)