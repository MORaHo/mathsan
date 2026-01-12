import decimal
from decimal import Decimal as dD
n = 1500

a = 1
p = 1
q = 1
s = 0

for k in range(a,n):
    for j in range(a,k+1):
        p *= -(6*j-1)*(2*j-1)*(6*j-5)
        q *= 10939058860032000*j**3
    s += (p/q) * (545140134*k+13591409)
    p = 1
    q = 1

decimal.getcontext().prec = 20
PI = float((dD(426880)*dD(10005).sqrt())/(dD(13591409)+dD(s)))
