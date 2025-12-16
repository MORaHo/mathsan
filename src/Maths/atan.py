from cmath import atan as arctangent
from src.LinAlg import ndarray,Matrix

def atan(x):
    if isinstance(x,ndarray):
        [rows,cols] = x.size()
        M = []
        for j in range(len(x)):
            for i in range(len(x[0])):
                M.append(arctangent(x[j][i]))
        return Matrix(M,rows,cols)
    else:
        return arctangent(x)