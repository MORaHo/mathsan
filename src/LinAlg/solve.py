import sys
from src.LinAlg.lu import lu
from src.LinAlg.qr import qr
from src.LinAlg.det import det
from src.LinAlg.chol import chol
from src.LinAlg.thomas import thomas
from src.LinAlg.hess_to_triang import triag
from src.LinAlg.ndarray import Matrix,Vector
from src.LinAlg.utils import zeros, tril, triu,diag, isequal

def forward_substitution(L:Matrix,b:Vector):

    b = b.col()
    y = []
    y.append(b[0]/L[0,0])

    for j in range(1,len(b)):
        b_j = b[j]
        for i in range(j):
            b_j -= L[j,i]*y[i]
        y.append(b_j/L[j,j])
    return Vector(y)

fwd_sub = forward_substitution

def backward_substitution(U:Matrix,y:Vector):
    y = y.col()
    n = len(y)-1
    x = zeros(n+1,1)
    [rows,cols] = U.size
    x[n] = y[-1]/U[rows-1,cols-1]

    for j in range(n-1,-1,-1):
        y_j = y[j]
        for i in range(n,j,-1):
            y_j -= U[j,i]*x[i]
        x[j] = y_j/U[j,j]
    return x

bkw_sub = backward_substitution

def solve(A:Matrix,b:Vector):

    [m,n] = A.size
    if m < n:
        raise('System cannot be solved, more unknowns than variables!')

    if m == n and det(A) == 0:
        print("Solution may not be unique!")

    #this will be expanded to handle more and more cases, initially I intend to add a QR solver and in the end for this function to basically become the \ of matlab

    # Following diagram in the algorithm section of https://uk.mathworks.com/help/matlab/ref/double.mldivide.html

    if m != n:
        [Q,R] = qr(A)
        Q1 = Q[:m,:n]
        R1 = R[:n,:n]
        y = Q1.T()*b.col()
        x = bkw_sub(R1,y)
    elif isequal(tril(A),A):
        x = fwd_sub(A,b)
    elif isequal(triu(A),A):
        x = bkw_sub(A,b)
    elif m <= 16:
        [L,U,P] = lu(A)
        y = fwd_sub(L,P*b)
        x = bkw_sub(U,y)
    else:
        if isequal((triu(A) + diag(diag(A,-1),-1)),A): #is the matrix upper-hessenberg
            if isequal((tril(A) + diag(diag(A,1),1)),A): #If matrix is tridiagonal
                #apply Thomas algorithm
                x = thomas(A,b)
            else:
                [U,Q] = triag(A) #decompose Hessenberg matrix into upper-triangular and Q (through givens rotations), which allows use to solve system
                y = Q.T()*b.col() #Q.T() = inv(Q)
                x = bkw_sub(U,y)

        else: #in any other case
            try: #try to apply cholesky
                L = chol(A)
                y = bkw_sub(L.T(),b)
                x = fwd_sub(L,y)
            except: #if cholesky fails (A is not symmetric positive definite) then apply LU factorization
                [L,U,P] = lu(A)
                y = fwd_sub(L,P*b)
                x = bkw_sub(U,y)
    return x
