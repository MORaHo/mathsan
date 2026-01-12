from src.LinAlg.ndarray import Matrix
from src.LinAlg.det import det
from src.LinAlg.utils import copy,eye
import sys


############################################
# This function utilizes Gauss-Jordan      #
# eliminiation to find the inverse matrix  #
############################################

def inv(M:Matrix):

    if len(M) != len(M[0]) or det(M) < 2E-18:
        print("Matrix is not invertible")
        sys.exit()

    A = copy(M)
    I = eye(len(M))

    for j in range(len(A)):
        A[j] = A[j] + I[j]

    for k in range(len(A)):

        largest_value = A[k,k]
        row = k
        for i in range(k,len(M)): #finding which line to pivot with
            if abs(A[i,k]) > abs(largest_value):
                largest_value = A[i,k]
                row = i

        if row != k: #pivoting
            temp = A[k]
            A[k]=A[row]
            A[row]=temp

        if A[k,k] == 0: #if even with pivoting it is 0, then we move onto the next row
            continue

        A_kk = A[k,k]
        for j in range(len(A)):

            if k == j: #we don't want to nullify the matrix
                continue

            l_jk = A[j,k]/A_kk
            A[j] = [ A[j,c]-l_jk*A[k,c] for c in range(len(A[0]))]


        for i in range(len(A[0])): #normalize all elements to make the elements on the left be ones
            A[k,i] = A[k,i]/A_kk

    end = len(A[0])

    for j in range(len(A)):
        A[j] = [ A[j,i] for i in range(len(A),end) ]

    return A
