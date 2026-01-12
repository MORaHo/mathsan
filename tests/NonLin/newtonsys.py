from src.LinAlg.ndarray import Vector,Matrix
from src.LinAlg.utils import isequal
from src.NonLin.newtonsys import newtonsys
from src.maths.cos import cos
from src.maths.sin import sin
from math import pi

EPS = 1E-6

func = lambda x: Vector([ x[0]**2+x[1]**2 -1 , sin(x[0]*pi/2)+x[1]**3 ])
J_func = lambda x: Matrix([[ 2*x[0] , 2*x[1] ],[ cos(x[0]*pi/2)*pi/2 , 3*x[1]**2 ]])
x0 = Vector([1,1])
max = 10

expected = Vector([0.476095822533,-0.879393408989]) #results from Matlab
result = newtonsys(func,J_func,x0,EPS,max)

if result[1] < EPS and isequal(expected,result[0]):
    print("Test passed!")
