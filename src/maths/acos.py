from cmath import acos as arccos
from src.LinAlg.ndarray import ndarray,Matrix

def acos(x):
    if isinstance(x,ndarray):
        [rows,cols] = x.size
        M = []
        for j in range(rows):
            for i in range(cols):
                M.append(arccos(x[j,i]).real)
        return Matrix(M,size=[rows,cols])
    else:
        return arccos(x).real
