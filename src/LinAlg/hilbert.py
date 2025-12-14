from src.LinAlg.ndarray import Matrix

def hilbert(n:int):
    
    H = []
    for m in range(n):
        H.append([ 1/(i+1) for i in range(m,m+n)])
    
    return Matrix(H)

hilb = hilbert