from src.LinAlg.ndarray import ndarray
from src.LinAlg.ndarray import Matrix,Vector
from typing import Union
numbers = Union[int,float,complex]
from src.LinAlg.utils import copy
from math import sqrt
from src.LinAlg.power import power,inv_power

def norm(M:ndarray,type_ = 2) -> numbers: #this will be changes to 2 when the spectral norm is implemented
    
    A = copy(M)
    [Arows,Acols] = A.size()
    
    if type(M) == Vector:
        match type_:
            
            case 1:
                norm = 0
                for i in range(Acols):
                    sum = 0
                    for j in range(Arows):
                        sum += abs(A.matrix[j][i])
                    if sum > norm:
                        norm = sum
                return norm

            case 100: #infinity norm but I can used infinity
                norm = 0
                for j in range(Arows):
                    sum = 0
                    for i in range(Acols):
                        sum += abs(A.matrix[j][i])
                    if sum > norm:
                        norm = sum
                return norm

            case 2: #Eucledian, 2 will be reserved for what will be the spectral norm or there will be a distinction between vector and matrix normss
                
                norm = 0
                for j in range(len(A)):
                    norm += A[j]**2
                
                return sqrt(norm)
            
    elif type(M) == Matrix:
        match type_:
            
            case 1:
                norm = 0
                for i in range(Acols):
                    sum = 0
                    for j in range(Arows):
                        sum += abs(A[j][i])
                    if sum > norm:
                        norm = sum
                return norm

            case 100: #infinity norm but I can used infinity
                norm = 0
                for j in range(Arows):
                    sum = 0
                    for i in range(Acols):
                        sum += abs(A[j][i])
                    if sum > norm:
                        norm = sum
                return norm

            case 2: #Eucledian, 2 will be reserved for what will be the spectral norm or there will be a distinction between vector and matrix normss
                
                M1 = A*A.T()
                M2 = A.T()*A
                [M1rows,M1cols] = M1.size()
                [M2rows,M2cols] = M2.size()
                if M1rows*M1cols > M2rows*M2cols:
                    M = A.T()*A
                else:
                    M = A*A.T()

                #I avoid using eig since for more ill-posed matrices the error increase
                max = sqrt(abs(power(M)[0]))
                min = sqrt(abs(inv_power(M)[0]))
                return max*min




