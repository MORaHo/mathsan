from src.LinAlg.utils import zeros
from src.LinAlg.ndarray import Vector

def polyval(p:Vector,xeval:Vector):

    n = len(p)
    xinit = xeval.col()
    x = len(xinit)
    xeval = zeros(x)
    for i in range(x):
        for j in range(n):
            xeval[i][0] += p[n-j-1] * xinit[i]**j

    return xeval

# We can also consider the case with small of number of points in x, and y = log(x) which will give large error near 0 as there polynomial will not be able to match the logarithmic descent to -infty with the small number of points given
#x = Vector([0.5,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
#y = sin(x)
#p = polyfit(x,y,16)
#xeval = linspace(0.6,10,101)
#print(polyval(p,xeval)-sin(xeval))