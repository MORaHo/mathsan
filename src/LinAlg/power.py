from src.LinAlg.ndarray import Matrix,Vector
from src.LinAlg.utils import ones
from src.LinAlg.inv import inv
from math import sqrt

toll = 2e-16 #tolerance we'll be using for power methods
nmax = 250 #maximum number of iterations 

def norm(v:Vector):
    norm = 0
    for j in range(len(v)):
        norm += v[j]**2

    return sqrt(norm)

def maxeig(A:Matrix):
    ## Implementation of the power method, used to find the largest eigenvalue
    
    [Arows,_] = A.size()
    x = ones(Arows) # initial guess
    y = x/norm(x)
    iter = 0
    rel_err = 1
    lambda_ = y.H() * A * y # eventhough its a 1x1 matrix it's still a matrix so to get the value it needs to be extracted

    while iter < nmax and rel_err > toll:
            
        x = A * y
        y = x/norm(x)
        old_lambda = lambda_
        lambda_ = y.H()*A *y # safe as a said before, Rayleigh quotient
        rel_err = abs(lambda_-old_lambda)/abs(lambda_) #this is the reason we need to extract the value
        iter += 1

    eigvalue = lambda_
    eigvector = x
    return [eigvalue,eigvector]

def mineig(A:Matrix):
    ## Implementation of the inverse power method to find the eigenvalue of minimum value
    invA = inv(A)
    return maxeig(invA)

power = power_method = maxeig
inv_power = inverse_power_method = inv_power_method = mineig

#A = Matrix([[1,1,0],[1,0,1],[0,1,1]])
#print(power(A)[0])