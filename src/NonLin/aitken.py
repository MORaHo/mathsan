from collections.abc import Callable

EPS = 1E-6

## Aitken's Accelerator
# Aitken's accelerator increases the speed of convergence of a given function to it's fixed point, the degree of acceleration depends on the original method's order of convergence.
# The accelerator also guarentees that methods that would otherwise not converge to effectively converge to the root of the base function.

def aitken(phi:Callable,x0,toll:float=EPS,kmax:int=1000):

    k = 0
    error = 1
    xvect = [x0]
    x_k = x0

    while error > toll and k < kmax:
        pk = phi(x_k)
        ppk = phi(pk)
        x_kp = x_k - ((pk-x_k)**2)/(ppk-2*pk+x_k)
        error = abs(x_kp - x_k)
        xvect.append(x_kp)
        x_k = x_kp
        k += 1 

    if error > toll:
        print("Aitken was unable to reach desired tollerance.")

    return [x_kp,k,error]