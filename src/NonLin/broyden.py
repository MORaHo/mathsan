from src.LinAlg.ndarray import Matrix,Vector
from src.LinAlg.solve import solve
from src.LinAlg.norm import norm

## Broyden's method 
# Broyden's method is a secant method inspired derivation of the Newton method for systems of non-linear equations.
# The method maintains the secant method's super-linear convergence, and the same loss of convergence degree when the root has higher multiplicity.

EPS = 1E-8
def broyden(B0:Matrix,f:Vector,x0:Vector,toll:float=EPS,kmax=1000) -> list[Vector,int]:

    k=0
    B_k = B0
    x_k = x0
    error = 1
    fk = f(x_k)
    while error > toll and k < kmax:

        delta_xk = solve(B_k,fk*-1)
        x_kp = x_k + delta_xk
        #delta_f = f(x_kp) - (x_k) #Broyden's method can be simplified so this step is not needed, so we are not going to compute this
        fkp = f(x_kp)
        B_k = B_k + (fkp*delta_xk.T())/(delta_xk.T()*delta_xk)
        error = norm(delta_xk,2)
        x_k = x_kp
        fk = fkp
        k += 1

    if error > toll:
        print("Broyden's method did not reach required tollerance.")
    
    return [x_k,k]






