from cmath import acosh as archyperbcos

from src.LinAlg.ndarray import Matrix, ndarray


def acosh(x):
    if isinstance(x, ndarray):
        [rows, cols] = x.size
        M = []
        for j in range(rows):
            for i in range(cols):
                M.append(archyperbcos(x[j,i]).real)
        return Matrix(M,size=x.size)
    else:
        return archyperbcos(x).real
