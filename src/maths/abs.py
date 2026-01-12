from src.LinAlg.ndarray import ndarray,Matrix

def absol(x):
    if isinstance(x,ndarray):
        [rows,cols] = x.size
        M = []
        for j in range(rows):
            for i in range(cols):
                M.append(abs(x[j,i]))
        return Matrix(M,size=[rows,cols])
    else:
        return abs(x)
