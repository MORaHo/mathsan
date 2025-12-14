from math import log as logarithm
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
        [rows,cols] = x.size()
        M = []
        for j in range(len(x)):
            for i in range(len(x[0])):
                M.append(logarithm(x[j][i],base))
        return Matrix(M,rows,cols)
    else:
        return logarithm(x[j][i],base)
