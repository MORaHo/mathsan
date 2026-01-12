from src.LinAlg.ndarray import Matrix
from src.LinAlg.utils import eye,zeros,copy
import sys

def LU_decomposition(A:Matrix):

    """
    Function that performs LU factorization of a matrix
    """

    #global U
    U = copy(A)
    [Urows,Ucols] = U.size

    if Urows != Ucols: # if the matrix is not square it will not work
        raise Exception("Matrix is not square")

    L = zeros(Urows,Ucols)
    P = eye(Urows)

    for k in range(Urows-1):
        largest_value = U[k,k]
        row = k

        for i in range(k,Urows): #check the with the largest number on the k-th column so we can pivot and reduce the error, also permit some matrices that wouldn't otherwise be able to be decomposed eventhough the fit the requirements to be decomposed.

            if abs(U[i,k]) > abs(largest_value):
                largest_value = U[i,k]
                row = i

        if row != k: #pivoting
            temp = U[k]
            U[k]=U[row]
            U[row]=temp
            temp = P[k]
            P[k] = P[row]
            P[row]=temp
            temp = L[k]
            L[k] = L[row]
            L[row] = temp

        A_kk = U[k,k]
        for j in range(k+1,Urows): # MEG and generating L matrix

            l_jk = U[j,k]/A_kk
            for c in range(0,Ucols):
                U[j,c] -= l_jk*U[k,c]
            L[j,k] = l_jk

    L += eye(Ucols)

    return [L,U,P]

lu = LU_decomposition

#A = Matrix([1,2,3,4,5,6,7,8,9],size=[3,3])
#[L,U,P] = lu(A)
#print(U)
