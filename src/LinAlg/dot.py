from src.LinAlg.ndarray import Matrix,Vector
from src.LinAlg import ROW_MAJOR

def dot(x:Vector,y:Vector) -> Matrix|int:

    if x.major == ROW_MAJOR != y.major == ROW_MAJOR and len(x) == len(y):

        [xrows,xcols] = x.size
        [yrows,ycols] = y.size


        M = Matrix([[0 for _ in range(xrows)] for _ in range(ycols)])
        for i in range(ycols):
            for j in range(xrows):
                sum = 0
                for k in range(xcols):
                    sum += x[j,k] * y.matrix[k,i]
                M[j,i] = sum

        if M.size == [1,1]:
            return M[0]
        else:
            return M

    else:
        raise Exception("Operation failed (dot.py): Dimensions are not the right form for a dot-product.")
