from src.LinAlg.ndarray import Vector
from src.Maths import cos
from math import pi

# This function generates a list of nodes generated according to Chebyshev-Gauss-Lobatto
# N is the number of sectors between the nodes, not the number of nodes itself.

def chebyshev(start,end,N:int):
    nodes = []

    for i in range(N+1):

        x_star = -cos(pi*i/N)
        x = (end+start)/2 + (end-start)*x_star/2
        nodes.append(x)

    return Vector(nodes)