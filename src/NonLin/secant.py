from collections.abc import Callable

## Secant method:
# The secant method is a method that emulates the newton method, without the explicit need for the derivative of the function for which we are trying to determine the root.
# For simple roots, this method converges with order: p = 1.618 (super-linear), this super-linear convergence is lost if the root has higher multiplicity that 1.

EPS = 1E-6
def secant(f:Callable,x0,x1,toll=EPS,kmax:int=1000) -> list[float,int,float]:

    x_km = x0 #x_{k-1}
    x_k = x1 #x_{k}
    xvect = [x0,x1]

    error = abs(x_km-x_k)
    k=0

    delta_f = lambda x_0,x_1: (f(x_1)-f(x_0))/(x_1-x_0)

    while error > toll and k < kmax:

        m = 1/delta_f(x_km,x_k)
        if m == 0:
            raise Exception('Stop due to annulment of df')
        x_kp = x_k - m*f(x_k)
        error = abs(x_kp-x_k)
        xvect.append(x_kp)
        k+=1
        x_km = x_k
        x_k = x_kp

    if error > toll:
        print("Secant method reached iteration limit.")

    return [x_k,k,error]


