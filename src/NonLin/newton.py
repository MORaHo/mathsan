import sys
from src.LinAlg.ndarray import Vector

def newton(x0:int,nmax:int,toll,f,df,mol:int):

    """
    Metodo di Newton per la ricerca degli zeri della
    funzione fun. Test d'arresto basato sul controllo
    della differenza tra due iterate successive.

    Input Parameters:

    x0         Initial Guess
    nmax       Iteration Limit
    toll       Result Tollerance
    f df   Anonymus functions containing the function and it's derivative
    mol        When mol=1 the classical Newton method is used, otherwise permette the modified Newton algorithm will be used.
    
    Exit Parameters:
    xvect      Vector containing all calcualted iterations, with the last being the final solution.
    it         Number of iterations completed
    """

    err = toll + 1
    it = 0
    xvect = []
    xv = x0

    while it < nmax and err > toll:
        dfx = df(xv)
        if dfx == 0:
            print('Stop due to annulment of df');
            sys.exit()
        else:
            xn = xv - mol*f(xv)/dfx
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