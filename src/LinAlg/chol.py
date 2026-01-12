from math import sqrt
from src.LinAlg.utils import copy
from src.LinAlg.ndarray import Matrix

def chol(A:Matrix):
    [m,_] = A.size
    L = copy(A)

    for k in range(m):

        L[k,k] = sqrt(L[k,k])

        for i in range(k+1,m):
            L[i,k] = L[i,k] / L[k,k]

        for j in range(k+1,m):
            for i in range(j,m):
                L[i,j] = L[i,j] - L[i,k]*L[j,k]

    for j in range(m):
        for i in range(m):
            if j < i:
                L[j,i] = 0

    return L
