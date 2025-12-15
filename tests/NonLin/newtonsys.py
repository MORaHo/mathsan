from src.LinAlg import Vector,Matrix,isequal
from src.NonLin import newton_sys
from src.Maths import cos,sin
from math import pi

EPS = 1E-6

func = lambda x: Vector([ x[0][0]**2+x[1][0]**2 -1 , sin(x[0][0]*pi/2)+x[1][0]**3 ])
J_func = lambda x: Matrix([[ 2*x[0][0] , 2*x[1][0] ],[ cos(x[0][0]*pi/2)*pi/2 , 3*x[1][0]**2 ]])
x0 = Vector([1,1])
max = 10

expected = Vector([0.476095822533,-0.879393408989]) #results from Matlab
result = newton_sys(func,J_func,x0,EPS,max)

if result[1] < EPS and isequal(expected,result[0]):
    print("Test passed!")