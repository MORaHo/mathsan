from math import sqrt
from src.LinAlg.utils import eye

# https://en.wikipedia.org/wiki/Givens_rotation

def sign(x):
    return 1*int(x>0) + 0*int(x==0) - 1*int(x<0)

def csr(a, b):
    if b == 0:
        c = sign(a)
        if (c == 0):
            c = 1.0
        s = 0
        r = abs(a)
    elif a == 0:
        c = 0
        s = -sign(b)
        r = abs(b)
    elif abs(a) > abs(b):
        t = b / a
        u = sign(a) * sqrt(1 + t * t)
        c = 1 / u
        s = -c * t
        r = a * u
    else:
        t = a / b
        u = sign(b) * sqrt(1 + t * t)
        s = -1 / u
        c = t / u
        r = b * u
    return [c, s, r]


def givens(a,b,g,s):
    G = eye(s)
    [c,s,r] = csr(a,b)
    G[g,g] = c
    G[g+1,g+1] = c
    G[g,g+1] = -s
    G[g+1,g] = s
    return G
