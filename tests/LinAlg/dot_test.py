from src.LinAlg.ndarray import Vector

v1 = Vector([1,2,3]).T()
v2 = Vector([1,2,3])

if v1*v2 != 14:
    raise Exception("Test failed(dot_test.py): Vector dot product not computing correctly.")