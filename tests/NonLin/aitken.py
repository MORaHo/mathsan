from src.NonLin.aitken import aitken
from src.LinAlg.utils import isequal
from src.Maths import log,exp

EPS = 1E-8

phi0 = lambda x: x+log(x)
phi1 = lambda x: (exp(x)+x)/(exp(x)+1)

results0 = aitken(phi0,x0=2,toll=1E-10)
results1 = aitken(phi1,x0=2,toll=1E-10)

expected0 = [1+0j,10]
expected1 = [1+0j,4]

if abs(results0[0]-expected0[0]) > EPS or abs(results1[0]-expected1[0]) > EPS or results0[1] != expected0[1] or results1[1] != expected1[1]:
    raise Exception("Aitken not functioning as expected.")

print("Aitken method test passed!")