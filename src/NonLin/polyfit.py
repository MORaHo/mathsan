from src.LinAlg import vand,solve,Vector

## See algorithm section: https://uk.mathworks.com/help/matlab/ref/polyfit.html

def polyfit(x_nodes:Vector,y_nodes:Vector,n:int):
    V = vand(x_nodes,n)
    p = solve(V,y_nodes)
    return p  #polynomial coefficient vector for x^n,x^(n-1),....,x,1

##TODO: MOVE TO TEST
#x = Vector([1,2,3,4,5])
#y = Vector([1,2,3,4,5])
#y = 1*(x**2)
#y = log(x)
#print(polyfit(x,y,2))