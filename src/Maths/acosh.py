from cmath import acosh as archyperbcos

from src.LinAlg import Matrix, ndarray


def acosh(x):
    if isinstance(x, ndarray):
        [rows, cols] = x.size()
        M = []
        for j in range(len(x)):
            for i in range(len(x[0])):
                M.append(archyperbcos(x[j][i]))
        return Matrix(M, rows, cols)
    else:
        return archyperbcos(x)
