from src.LinAlg.utils import eye,isequal
from src.LinAlg.ndarray import Vector
from src.NonLin.broyden import broyden
from src.maths.sin import sin
from math import pi

B0 = eye(2)
x0 = Vector([1,1])
EPS = 10E-6
f = lambda x: Vector([x[0]**2 + x[1]**2-1,sin(pi*x[0]/2)+x[1]**3])
result = broyden(B0,f,x0,EPS)

expected = Vector([0.476095822533,-0.879393408989]) #test and result from Calcolo Scientifico by Alfio Quarteroni

if result[1] > 10 or not isequal(expected,result[0]):
    raise Exception("Result's of Broyden's method test not as expected!")

print("Broyden's method test passed!")
