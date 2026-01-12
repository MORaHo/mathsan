from src.misc.linspace import linspace

def trapezoid(a,b,N:int,f):

    h = (b-a)/N
    x = linspace(a+h,b-h,N-2)
    I = h * (0.5*f(a) + f(x).sum() + 0.5*f(b))

    return I
