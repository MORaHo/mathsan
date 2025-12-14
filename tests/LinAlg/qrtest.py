from src.LinAlg.utils import isequal
from src.LinAlg.ndarray import Matrix
from src.LinAlg.qr import qr_householder as qr

A = Matrix([[12,-51,4],[6,167,-68],[-4,24,-41]])
#A = Matrix([[124,61,135],[31,129,10],[71,7,73],[95,87,56]])
[Q,R] = qr(A)

if not isequal(A,Q*R):
    print("Householder-rotation-based QR decomposition not working")