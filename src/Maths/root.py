from src.LinAlg import ndarray,Matrix

def root(x,n:int):
    if isinstance(x,ndarray):
        [rows,cols] = x.size()
        M = []
        for j in range(len(x)):
            for i in range(len(x[0])):
                M.append((x[j][i])**(1/n))
        return Matrix(M,rows,cols)
    else:
        return x**(1/n)