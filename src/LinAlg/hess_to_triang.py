from src.LinAlg.utils import eye
from src.LinAlg.givens import givens
from src.LinAlg.ndarray import Matrix

toll = 2e-16 #tolerance we'll be using for power methods
nmax = 250 #maximum number of iterations

# currenctly using this gives a lot of error so for now I wull substitute with a LU decomposition

def triag(A:Matrix):

    n = len(A)
    Q = eye(n)
    for i in range(0,n-1):
        G_i = givens(A[i,i],A[i+1,i],i,n)
        Q *= G_i.T()
        A = G_i*A
    return [A,Q]
