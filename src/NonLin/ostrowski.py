import sys
from src.LinAlg.ndarray import Vector

def ostrowski(x0:int,nmax:int,toll,f,df,mol:int):

    err = toll + 1
    it = 0
    xvect = []
    xv = x0

    while it < nmax and err > toll:
        dfx = df(xv)
        print(xv)
        if dfx == 0:
            print('Stop due to annulment of df');
            sys.exit()
        else:
            yn = xv - mol*f(xv)/dfx
            xn = yn - (f(yn)*(xv-yn))/(f(xv)-2*f(yn))
            err = abs(xn-xv)
            xvect.append(xn)
            it = it+1
            xv = xn

    if (it < nmax):
        print(' Converged in',it,'iterations');
    else:
        print('Iteration limit reached')
    print('Calculated root: ',xvect[-1])
    return [Vector(xvect),it]

