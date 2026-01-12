from src.LinAlg.ndarray import ndarray,Matrix

def root(x,n:int):
    if isinstance(x,ndarray):
        [rows, cols] = x.size
        M = []
        for j in range(rows):
            for i in range(cols):
                M.append((x[j,i])**(1/n))
        return Matrix(M,size=x.size)
    else:
        return x**(1/n)
