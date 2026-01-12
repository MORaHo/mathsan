from cmath import cos as cosine
from src.LinAlg.ndarray import ndarray,Matrix

def cos(x):
    if isinstance(x,ndarray):
        [rows, cols] = x.size
        M = []
        for j in range(rows):
            for i in range(cols):
                M.append(cosine(x[j,i]).real)
        return Matrix(M,size=x.size)
    else:
        return cosine(x).real
