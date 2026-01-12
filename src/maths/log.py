from cmath import log as logarithm
from src.LinAlg.ndarray import ndarray,Matrix,Vector

def ln(x,base):
    return logarithm(x)

def logwithbase(x,base:int):
    return logarithm(x,base)

def log(x:Vector,base:int=0):
    if base != 0:
        logarithm = logwithbase
    else:
        logarithm = ln

    if isinstance(x,ndarray):
        [rows, cols] = x.size
        M = []
        for j in range(rows):
            for i in range(cols):
                M.append(logarithm(x[j,i],base))
        return Matrix(M,size=x.size)
    else:
        return logarithm(x,base)
