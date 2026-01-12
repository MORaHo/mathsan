from src.LinAlg.ndarray import Matrix
from src.LinAlg.lu import lu

def det(A:Matrix):
    [Arows,_] = A.size
    [_,U,_] = lu(A)
    det = 1
    for i in range(Arows):
        det *= U[i,i]
    return det
