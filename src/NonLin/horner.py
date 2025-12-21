from src.LinAlg.ndarray import Vector
from src.LinAlg.utils import zeros

# Horner's method deflates a given polynomial around the root which is being determined.
# It output is the same polynomial equation which was inputted but with the root that was being reached for removed, reducing the polynomial by one degree.

def horner(a:Vector,z:float):
    n = len(a)
    b = zeros(n,1)
    b[0] = a[0]
    for j in range(1,n):
        b[j] = a[j] + b[j-1] * z
    b0 = b[-1] #b_0
    b = b[0:n-1] #q_{n-1}
    return [b0,b]

a = Vector([1,-2,0,-4])
z = 3
horner(a,1)
