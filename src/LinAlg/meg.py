from src.LinAlg.ndarray import Matrix
from src.LinAlg.utils import copy

def gaussian_elimination(A:Matrix):
    
    M = copy(A)
    [Mrows,Mcols] = M.size()
    for k in range(Mrows-1):
        
        largest_value = M[k][k]
        row = k 
        for i in range(k,Mrows):
            if abs(M[i][k]) > abs(largest_value):
                largest_value = M[i][k]
                row = i

        if row != k: #pivoting
            temp = M[k]
            M[k]=M[row]
            M[row]=temp
       
        if M[k][k] == 0:
            continue

        A_kk = M[k][k]
        for j in range(k+1,Mrows):

            l_kj = M[j][k]/A_kk
            M[j] = [ M[j][c]-l_kj*M[k][c] for c in range(0,Mcols)]

    return M

meg = ref = gaussian_elimination  


