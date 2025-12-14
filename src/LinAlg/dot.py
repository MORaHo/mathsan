from src.LinAlg.ndarray import Matrix,Vector

def dot(x:Vector,y:Vector) -> Matrix|int:
        
    if x.is_row != y.is_row and len(x) == len(y):
        

        
        M = Matrix([[0 for _ in range(x.size()[0])] for _ in range(y.size()[1])])
        for i in range(y.size()[1]):
            for j in range(x.size()[0]):
                sum = 0
                for k in range(x.size()[1]):
                    sum += x[j][k] * y.matrix[k][i]
                M[j][i] = sum
        
        if M.size() == [1,1]:
            return M[0]
        
        return M
    
    else:
        print("Operation failed (dot.py): Dimensions are not the right form for a dot-product.")
