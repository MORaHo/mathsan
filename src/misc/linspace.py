from src.LinAlg.ndarray import Vector

def linspace(a, b, n:int=100):
    if n < 2:
        return b
    diff = (float(b) - a)/(n - 1)
    return Vector([a + diff*i  for i in range(n)])