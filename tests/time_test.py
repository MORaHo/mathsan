from src.LinAlg.utils import eye,diag
from src.LinAlg.solve import solve
from src.misc.linspace import linspace

A1 = eye(1000)*4
print("1")
A2 = diag(diag(eye(999)*-2),-1)
print("2")
A3 = diag(diag(eye(999)*-2),1)
print("3")
A = A1+A2+A3
print("+")
b = linspace(1,1000,1000)
print("b")
b = b**2
print("b2")
x = solve(A,b)
print(x)
