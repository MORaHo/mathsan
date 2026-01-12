from math import pi
from src.maths.cos import cos
from src.NonLin.bisection import bisection

EPS = 1E-6
func = lambda x: cos(x)
if abs(pi/2+bisection(-3,0,func))<EPS:
    print("Test passed!")
