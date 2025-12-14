from src.Misc.linspace import linspace
from src.LinAlg.ndarray import Vector

def simpson(a,b,N,f):
    
    h = (b-a)/N
    x = linspace(a,b,2*N+1)
    y = f(x)
    evens = Vector(y[1:2*N:2])
    odds = Vector(y[2:2*N-1:2])
    I = h/6 * (y[0] + 2 * odds.sum() +4*evens.sum() +y[-1])

    return I