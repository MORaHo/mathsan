from cmath import tan as tangent
from src.LinAlg import ndarray,Matrix

def tan(x):
    if isinstance(x,ndarray):
        [rows,cols] = x.size()
        M = []
        for j in range(len(x)):
            for i in range(len(x[0])):
                M.append(tangent(x[j][i]))
        return Matrix(M,rows,cols)
    else:
        return tangent(x)