from src.misc.linspace import linspace

def midpoint(a,b,N:int,f):

    h = (b-a)/N
    x = linspace(a+h/2,b-h/2,N)
    I = h * f(x).sum()

    return I
