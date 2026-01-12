import sys
from tokenize import COLON
from typing import Union
from src.LinAlg import ROW_MAJOR,COLUMN_MAJOR
from src.LinAlg.ndarray import ndarray
from src.LinAlg.ndarray import Matrix,Vector

numbers = Union[int,float,complex]
toll = 2E-8

def eye(n:int) -> (Vector | Matrix):
    I = [ 1 if i%n == i//n else 0 for i in range(n*n) ]
    return Matrix(data=I,size=[n,n])

def ones(m:int,n:int=1) -> (Vector | Matrix):
    Z = [ 1 for _ in range(m*n) ]
    return Matrix(data=Z,size=[m,n])

def zeros(m:int,n:int=1) -> (Vector | Matrix):
    Z = [ 0 for _ in range(m*n) ]
    return Matrix(data=Z,size=[m,n])

def copy(A:ndarray)-> Matrix:
    csize = A.size
    C = []
    for i in range(len(A)):
        C.append(A.matrix[i])
    oldmajor = A.major
    return Matrix(data=C,size=csize,major=oldmajor,preserve_flag=True)

def diag(A:ndarray,offset_:int=0) -> (Vector | Matrix):

    [rows,cols] = A.size

    if type(A) ==  Vector:

        D = []
        step_y = cols*int(A.major == ROW_MAJOR) + 1*int(A.major != COLUMN_MAJOR)
        step_x = 1*int(A.major == ROW_MAJOR) + rows*int(A.major != COLUMN_MAJOR)
        dim  = len(A)+abs(offset_)
        shift_x = int(offset_>0)
        shift_y = int(offset_<0)
        for i in range(dim*dim):
            row = i // cols
            col = i % cols
            if shift_x*(row-offset_==col) or shift_y*(col-offset_==row):
                k = row * step_y + col * step_x
                D.append(A.matrix[k])
            else:
                D.append(0)

        return Matrix(data=D,size=[dim,dim],major=ROW_MAJOR)

    elif rows == cols: # matrix is a square matrix so we create a vector

        v = []
        dim = rows - abs(offset_)
        step_x = 1*int(A.major == ROW_MAJOR) + rows*int(A.major != ROW_MAJOR)
        step_y = cols*int(A.major == ROW_MAJOR) + 1*int(A.major != ROW_MAJOR)
        shift_x = (offset_>0)*(1*int(A.major == ROW_MAJOR) + rows*int(A.major != ROW_MAJOR))
        shift_y = (offset_<0)*(cols*int(A.major == ROW_MAJOR) + 1*int(A.major != ROW_MAJOR))
        for i in range(dim):
            k = shift_y + shift_x + i*(1+rows) #since the diagonal will always be 1 plus rows or cols, and rows==cols
            v.append(A.matrix[k])
        return Vector(v)

    else:
        raise Exception("Matrix is not vector or square matrix")

def tril(A:Matrix) -> Matrix:
    rows,cols = A.size
    M = []
    step = cols*int(A.major == ROW_MAJOR) + rows*int(A.major != ROW_MAJOR)
    if A.major == ROW_MAJOR:
        for i in range(rows*cols):
            if i//step >= i%step:
                M.append(A.matrix[i])
            else:
                M.append(0)
    else:
        for i in range(rows*cols):
            if i//step <= i%step:
                M.append(A.matrix[i])
            else:
                M.append(0)
    return Matrix(data=M,size=A.size,major=A.major,preserve_flag=True)

def triu(A:Matrix) -> Matrix:
    rows,cols = A.size
    M = []
    step = cols*int(A.major == ROW_MAJOR) + rows*int(A.major != ROW_MAJOR)
    if A.major != ROW_MAJOR:
        for i in range(rows*cols):
            if i//step >= i%step:
                M.append(A.matrix[i])
            else:
                M.append(0)
    else:
        for i in range(rows*cols):
            if i//step <= i%step:
                M.append(A.matrix[i])
            else:
                M.append(0)
    return Matrix(data=M,size=A.size,major=A.major,preserve_flag=True)

def linspace(a, b, n:int=100) -> Vector:
    if n < 2:
        return b
    diff = (float(b) - a)/(n - 1)
    return Vector([a + diff*i  for i in range(n)])

def ndabs(A:ndarray): #absolute value for ndarrays
    M = []
    [rows,cols] = A.size
    for j in range(rows*cols):
        M.append(abs(A.matrix[j]))
    return Matrix(data=M,size=A.size,major=A.major,preserve_flag=True)

def isequal(A:ndarray,B:ndarray):

    if type(A) is not type(B):
        raise Exception("Input-types do not match")
    if A.size != B.size:
        raise Exception("Dimensions of matrices being compared do not match")

    [n,m] = A.size

    if type(A) in numbers.__args__:
        return A == B
    if type(A) is Vector:
        for j in range(len(A)):
            if abs(A[j] - B[j]) > toll:
                return False
        return True
    if type(A) is Matrix or type(A) is ndarray:
        for j in range(m):
            for i in range(n):
                if abs(A[j,i] - B[j,i]) > toll:
                    return False
        return True
    else:
        try:
            return A==B
        except:
            raise Exception("Equality determination for implemented for input of type:"+ str(type(A)))

#A = zeros(5,5)
#x = diag(A,1)
#print('done')
