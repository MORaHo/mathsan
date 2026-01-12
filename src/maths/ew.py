import sys
from src.LinAlg.ndarray import ndarray,Matrix,Vector

## This is element wise multiplication for matrices, which is useful when using methods which require lambda functions which can take vectors but require only element wise multiplcation
## This is an equivalent to .* in matlab, and I have called ew for element-wise multiplication, and since the solution is ugly it makes it easier to remember the name

def ew(x:ndarray,y:ndarray):
    if x.size != y.size:
        print("Matrices are not the same size")
        sys.exit()
    [rows,cols] = x.size
    M = []
    for j in range(rows):
        for i in range(cols):
            M.append(x[j,i]*y[j,i])
    if type(x) is Vector:
        return Vector(M,axis=int(cols>1))
    else:
        return Matrix(M,size=x.size)
