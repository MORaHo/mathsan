from src.LinAlg.ndarray import Matrix,Vector

def vandermonde(x:Vector,n:int):
    
    V = []
    x = x.col() #making sure it's a column vector

    for m in range(len(x)):
        V.append([ x[m]**i for i in range(n,-1,-1)])
    
    return Matrix(V)

vand = vander = vandermonde
