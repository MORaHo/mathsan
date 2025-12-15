import sys
from typing import Union
from src.LinAlg.ndarray import ndarray
from src.LinAlg.ndarray import Matrix,Vector

numbers = Union[int,float,complex]
toll = 2E-8

def eye(n:int) -> (Vector | Matrix):
    I = [ [ 1 if i == j else 0 for j in range(n) ] for i in range(n) ]
    return Matrix(I)

def ones(m:int,n:int=1) -> (Vector | Matrix):
    Z = [ [ 1 for _ in range(n) ] for _ in range(m) ]
    return Matrix(Z)

def zeros(m:int,n:int=1) -> (Vector | Matrix):
    Z = [ [ 0 for _ in range(n) ] for _ in range(m) ]
    return Matrix(Z)

def copy(A:ndarray)-> Matrix:
    [Arows,Acols] = A.size()
    N = [[ A.matrix[j][i] for i in range(Acols)] for j in range(Arows)]
    return Matrix(N)

def diag(A:ndarray,offset_:int=0) -> (Vector | Matrix):

    [Arows,Acols] = A.size()

    if type(A) == Vector: # matrix is a vector so we create a matrix

        shift_y = (offset_ < 0)
        shift_x = (offset_ > 0)
        zero_case = (offset_ == 0) #without this there would need to be a if statement to handle the case where offset_ = 0

        column = (Arows>1) #allows use to handle both column and row vectors
        row = (Acols>1)

        dim = len(A)*abs(offset_)
        B = zeros(dim,dim)

        for i in range(dim):
            for j in range(dim):  
                if i-shift_x*offset_ == j+shift_y*offset_:       
                    
                    #allow use handle positive, negative and null offsets, as well as row and column vectors 
                    A_j = shift_x*column*j + shift_y*column*i + zero_case*column*j
                    A_i = shift_y*row*i + shift_x*row*j + zero_case*row*i

                    B[j][i] = A.matrix[A_j][A_i]
        return B
                    

    elif Arows == Acols: # matrix is a square matrix so we create a vector

        shift_y = (offset_ < 0) #one of the two shifts will be true, if offset_ is non-zero
        shift_x = (offset_ > 0)
        B = []
        
        # I tried to use list comprehension, but it didn't seem to work
        for i in range(Arows):
            for j in range(Acols):
                if i-shift_x*offset_ == j+shift_y*offset_: #it needs to be added to j since it positive
                    B.append([A[j][i]])
        
        return Vector(B)

    else:
        print("Matrix is not vector or square matrix")
        sys.exit()

def tril(A:Matrix) -> Matrix:
    n,m = A.size() # m = Arows and n = Acols, to avoid rewriting a lot
    M = zeros(n,m)
    for i in range(n):
        for j in range(m):
            if i >= j:
                M[i][j] = A[i][j]
    return M

def triu(A:Matrix) -> Matrix:
    n,m = A.size() # m = Arows and n = Acols, to avoid rewriting a lot
    M = zeros(n,m)
    for i in range(n):
        for j in range(m):
            if i <= j:
                M[i][j] = A[i][j]
    return M

def linspace(a, b, n:int=100) -> Vector:
    if n < 2:
        return b
    diff = (float(b) - a)/(n - 1)
    return Vector([a + diff*i  for i in range(n)])

def ndabs(A:ndarray): #absolute value for ndarrays
    M = copy(A)
    [Mrows,Mcols] = M.size()
    for j in range(Mrows):
        for i in range(Mcols):
            M[j][i] = abs(M.matrix[j][i])
    return M

def isequal(A:ndarray,B:ndarray):
    [mA,nA] = A.size()
    [mB,nB] = B.size()

    if (mA != mB) or (nA != nB):
        print("Dimensions of matrices being compared do not match")
        sys.exit()
    
    n = nA
    m = mA

    for j in range(m):
        for i in range(n):
            if abs(A.matrix[j][i] - B.matrix[j][i]) > toll:
                return False
    return True
