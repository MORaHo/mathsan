from src.LinAlg.ndarray import Vector
from src.LinAlg.utils import zeros
from src.NonLin.horner import horner

EPS = 1E-8

def newtonhorner(a:Vector,x0:float=1,toll:float=EPS,kmax:int=1000) -> list[Vector,Vector]:

    n = len(a) - 1
    roots = zeros(n,1)
    iter = zeros(n,1)

    for k in range(n):

        niter = 0
        x_k = x0
        error = 1

        while error > toll and niter < kmax:
            [pz,b] = horner(a,x_k)
            [dpz,b] = horner(b,x_k)
            x_kp = x_k - pz/dpz
            error = abs(x_kp-x_k)
            x_k = x_kp
            niter += 1

        if niter==kmax or error>toll:
            print("Newton-Horner did not converge to the desired number.")

        # Having determined an adequate value for the root through this modified version of the Newton method. We can now
        # deflate the polynomial with the roots estimate, and determine the deflated polynomial to determine the next root
        [pz,a] = horner(a,x_k)
        roots[k] = x_k
        iter[k] = niter

    return [roots,iter]

#a = Vector([1,-6,11,-6])
#[x,iter] = newtonhorner(a,0,1E-15,100)
#print(x) # [1,2,3]
#print(iter) # [8,8,2]

#a = Vector([1,-7,15,-13,4])
#[x,iter] = newtonhorner(a,0,1E-15,100)
#print(x) # [ 1,1,1,4 ]
#print(iter) # [ 61,100,6,2 ]
