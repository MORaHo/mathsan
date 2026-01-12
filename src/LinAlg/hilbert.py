from src.LinAlg.ndarray import Matrix

def hilbert(n:int):

    H = []
    for m in range(n):
        for i in range(m,m+n):
            H.append(1/(i+1))

    return Matrix(H,size = [n,n])

hilb = hilbert
