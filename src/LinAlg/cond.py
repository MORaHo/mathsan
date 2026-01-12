from math import sqrt
from src.LinAlg.ndarray import Matrix
from src.LinAlg.power import power,inv_power

### This function is subject to possible change

def cond(A:Matrix):

    M1 = A*A.T()
    M2 = A.T()*A
    [M1rows,M1cols] = M1.size
    [M2rows,M2cols] = M2.size
    if M1rows*M1cols > M2rows*M2cols:
        M = A.T()*A
    else:
        M = A*A.T()

    #I avoid using eig, since for more ill-posed matrices the error increase
    max = sqrt(abs(power(M)[0])) #index 0 is for the eigenvalue, since the function also returns the eigenvector
    min = sqrt(abs(inv_power(M)[0]))
    return max*min
