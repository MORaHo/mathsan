import sys
from typing import Union

numbers  = Union[int,float,complex]

##---------------##
#| NDARRAY CLASS |#
##---------------##

class ndarray():

    def __init__(self,data,rows:int,columns:int):

        try:

            if type(data[0])==list:
                data_size = len(data)*len(data[0])
            else: 
                data_size = len(data)

            if data_size != rows*columns:
                print("Data doesn't fit in the size parameters.")
                sys.exit()

            if type(data) == list and type(data[0]) == list: #if the input data is already a 2d array
                self.matrix = data
            else:
                self.matrix = [ data[ r*columns:r*columns+columns ] for r in range(rows) ]
        except:
            self.matrix = []
    
    def T(self): #returns matrix transpose

        T = [ [ self[j][i] for j in range(len(self)) ] for i in range(len(self[0])) ]
        return ndarray(T, rows=len(self[0]), columns=len(self))

    def H(self): #complex conjugate equivalent of the tranpose

        M = self.matrix
        H = [ [ conj(M[j][i]) if type(M[j][i]) == complex else M[j][i] for j in range(len(M)) ] for i in range(len(M[0])) ]
        return ndarray(H,len(H),len(H[0]))
    
    def __str__(self):
        """Prints matrix in Matlab style, although the variable name is not printed"""
        string = "\n"
        
        for j in range(len(self.matrix)):
            string += "  "
            for i in range(len(self.matrix[0])):
                number = format(float(self.matrix[j][i]),'.4')
                string += str(number)
                string += "  "
            string += ("\n" + (j<len(self.matrix)-1)*"\n")
        return string
    
    def __len__(self):
        return len(self.matrix)
    
    def __getitem__(self,index):

        
        if type(index)==int:
            return self.matrix[index]

        elif type(index)==slice:
            return self.matrix[index]

        try:

            if type(index)==tuple and len(index)==2:

                y,x = index

                if type(y) == slice:
                    y_start = int(0 if y.start == None else y.start)
                    y_end = int(len(self) if y.stop == None else y.stop)
                elif type(y) == int:
                    y_start = y
                    y_end = y+1
                if type(x) == slice:
                    x_start = int(0 if x.start == None else x.start)
                    x_end = int(len(self[0]) if x.stop == None else x.stop)
                elif type(x) == int:
                    x_start = x
                    x_end = x + 1
       
                M = [ [self[j][i] for i in range(x_start,x_end) ] for j in range(y_start,y_end) ]

                if [len(M),len(M[0])] != [1,1]:
                    return ndarray(M)
                else:
                    return M[0][0]
        
        except:
            return []
        
    def __add__(self,B): # addition

        if type(self) == type(B) and len(self) == len(B) and len(self[0]) == len(B[0]):
            C = [ [ self[i][j]+B[i][j] for j in range(len(B[0])) ] for i in range(len(B)) ]
            return ndarray(C)
        else:
            print("Matrix dimensions or types don't match! (Addition)")
            sys.exit()

    def __sub__(self,s): #subdivision

        if type(self) != type(s) or len(self) != len(s) or len(self[0]) != len(s[0]):
            print("Matrix dimensions or types do not match! (Subtraction)")
            sys.exit()        

        S = [ [ 0 for _ in range(len(self[0])) ] for _ in range(len(self)) ]
        for i in range(len(self)):
            for j in range(len(self[0])):
                S[i][j] = self[i][j] - s[i][j]
            
        return ndarray(S)

##--------------##
#| MATRIX CLASS |#
##--------------##

class Matrix(ndarray):

    __array_priority__ = 2

    def __new__(cls,data,rows:int=0,columns:int=0):
        if rows < 2 or columns < 2:
            if columns == 0 and len(data) == 1: #it's a row 
                return Vector(data,is_row = 1)
            try:
                if len(data[0]) == 1:
                    return Vector(data)
                else:
                    return super(Matrix, cls).__new__(cls)
            except:
                return Vector(data)

        else:
            return super(Matrix, cls).__new__(cls)

    def __init__(self,data,rows:int=0,columns:int=0):

        rows = rows*(rows!=0)+len(data)*(rows==0)
        try:
            columns = columns*(columns!=0)+len(data[0])*(columns==0)
        except:
            columns = columns
        super().__init__(data=data,rows = rows,columns = columns)

    def T(self): #returns matrix transpose
        T = [ [ self[j][i] for j in range(len(self)) ] for i in range(len(self[0])) ]
        return Matrix(T, rows=len(self[0]), columns=len(self))

    def H(self): #complex conjugate equivalent of the tranpose

        M = self.matrix
        H = [ [ conj(M[j][i]) if type(M[j][i]) == complex else M[j][i] for j in range(len(M)) ] for i in range(len(M[0])) ]
        return Matrix(H,len(H),len(H[0]))
    
    def __getitem__(self,index):

        
        if type(index)==int:
            return self.matrix[index]

        elif type(index)==slice:
            return self.matrix[index]

        try:

            if type(index)==tuple and len(index)==2:

                y,x = index

                if type(y) == slice:
                    y_start = int(0 if y.start == None else y.start)
                    y_end = int(len(self) if y.stop == None else y.stop)
                elif type(y) == int:
                    y_start = y
                    y_end = y+1
                if type(x) == slice:
                    x_start = int(0 if x.start == None else x.start)
                    x_end = int(len(self[0]) if x.stop == None else x.stop)
                elif type(x) == int:
                    x_start = x
                    x_end = x + 1
       
                M = [ [self[j][i] for i in range(x_start,x_end) ] for j in range(y_start,y_end) ]

                if [len(M),len(M[0])] != [1,1]:
                    return Matrix(M)
                else:
                    return M[0][0]
        
        except:
            return []
    
    def __setitem__(self,index,item):

        if type(index)==tuple and len(index)==2:
                
            y,x = index

            if type(item) == Matrix:

                i_n,i_m = item.size()
    
                if type(y) == slice and type(x) == slice:

                    y_start = int(0 if y.start == None else y.start)
                    y_end = int(len(self.matrix) if y.stop == None else y.stop)
                    x_start = int(0 if x.start == None else x.start)
                    x_end = int(len(self.matrix[0]) if x.stop == None else x.stop)

                    if i_n != (y_end-y_start) or i_m != (x_end-x_start):
                        raise Exception("Item change dimensions do not match, check the what you are trying to change (matrix input case)")

                    for j in range(y_start,y_end):
                        for i in range(x_start,x_end):
                            self[j][i] = item[j-y_start][i-x_start]

                    
                if type(y) == slice and type(x) == int:
                    
                    y_start = int(0 if y.start == None else y.start)
                    y_end = int(len(self) if y.stop == None else y.stop)

                    if i_n != (y_end-y_start):
                        raise Exception("Item change dimensions do not match, check the what you are trying to change (column vector case)")
                    
                    for j in range(y_start,y_end):
                            self[j][x] = item[j-y_start][x]
                
                elif type(y) == int and type(x) == slice:

                    x_start = int(0 if x.start == None else x.start)
                    x_end = int(len(self[0]) if x.stop == None else x.stop)

                    if i_n != (x_end-x_start):
                        raise Exception("Item change dimensions do not match, check the what you are trying to change (row vector case)")
                    
                    for j in range(x_start,x_end):
                            self[x][j] = item[x][j-x_start]

            elif type(item) == Vector:
                
                i_n = len(item)
                if item.is_row: #it's a row vector
                    start = int(0 if x.start == None else x.start)
                    end = int(len(self[0]) if x.stop == None else x.stop)+1
                    if type(y) != int:
                        raise Exception("Item dimensions too large, it is row vector, so cannot span multipe rows")
                else:
                    start = int(0 if y.start == None else y.start)
                    end = int(len(self) if y.stop == None else y.stop)+1
                    if type(x) != int:
                        raise Exception("Item dimensions too large, it is column vector, so cannot span multipe columns")

                if i_n != (end-start):
                    raise Exception("Item change dimensions do not match, check the what you are trying to change")
                
                if item.is_row: #again, row vector
                    for j in range(start,end):
                        self[y][j] = item[j-start]    
                else:
                    for j in range(start,end):
                        self[j][x] = item[j-start]
                

            elif type(item) in numbers.__args__:
                
                if type(x) != int or type(y) != int:
                    raise Exception("Input size does not match")
                
                self.matrix[y][x] = item
        
        else:
            self.matrix[index] = item  
    
    def __add__(self,B): # addition

        if type(self) == type(B) and B.size() == self.size():
            C = [ [ self[i][j]+B[i][j] for j in range(len(B[0])) ] for i in range(len(B)) ]
            return Matrix(C)
        else:
            raise Exception("Matrix dimensions or types don't match! (Addition)")

    def __sub__(self,s): #subdivision

        if type(s) != Matrix or self.size() != s.size():
            raise Exception("Matrix dimensions or types do not match! (Subtraction)")      

        [rows,columns] = self.size()
        S = Matrix([ [ 0 for _ in range(columns) ] for _ in range(rows) ])

        for i in range(rows):
            for j in range(columns):
                S[i][j] = self[i][j] - s[i][j]
        return S

    def __mul__(self,B): # element-wise scalar multiplication and dot product

        [rows,columns] = self.size() #rows,columns

        if type(B) in numbers.__args__: #allows element wise moltiplication by scalar with the matrix
            
            Z = [[ B*self[j,i] for i in range(columns)] for j in range(rows)]

            return Matrix(Z)

        elif columns != B.size()[0]: #if the dimensions don't match the dotproduct cannot be performed
            raise Exception("Dimensions of the two matrices don't match")

        new_columns = B.size()[1]
        Z = Matrix([[ 0 for _ in range(new_columns)] for _ in range(rows)])
        
        #dot-product
        for i in range(new_columns):
            for j in range(rows):
                sum = 0
                for k in range(columns):
                    sum += self[j,k] * B.matrix[k][i]
                Z[j,i] = sum
        
        if [rows,new_columns] == [1,1]:
            return Z[0][0]
        else:
            return Z
        
    def __rmul__(self,m):
        return self.__mul__(m)

    def __truediv__(self,s): #element-wise division
        [n,m] = self.size()
        S = [[self[j][i]/s  for i in range(m) ] for j in range(n)]
        return Matrix(S)
    
    def __pow__(self,b):
        
        if type(b) == int or type(b) == float:
            I = []
            [rows,cols] = self.size()
            for j in range(rows):
                for i in range(cols):
                    I.append(self[j][i] ** b)
            return Matrix(I,rows,cols)
        
        # matmul didn't work for some reason I just chose to repurpose the power operator to permit element-wise matrix multiplication
        # this will be useful when discretizing for non-linear analysis and solving ODEs
        elif isinstance(b,ndarray):

            if self.size() != b.size():
                raise Exception("Dimensions do not match for element-wise multiplication")
            
            [rows,cols] = self.size()
            P = []
            for j in range(rows):
                for i in range(cols):
                    P.append(self[j][i] * b[j][i])
            return Matrix(P,rows,cols)
        
    def size(self):
        # returns [rows,columns]
        return [len(self),len(self[0])]

##--------------##
#| VECTOR CLASS |#
##--------------##

class Vector(ndarray):

    __array_priority__ = 1

    def __init__(self,data,is_row:bool=False):
        if is_row and type(data[0]) != list:
            self.is_row = is_row
            rows = 1
            cols = len(data)
            super().__init__(data,rows,cols)
        elif len(data) == 1 and type(data[0]) == list:
            self.is_row = True
            rows = 1
            cols = len(data[0])
            super().__init__(data,rows,cols)
        elif len(data) == 1:
            self.is_row = True
            rows = 1
            cols = 1
            super().__init__(data,rows,cols)
        else:
            self.is_row = False
            rows = len(data)
            cols = 1
            super().__init__(data,rows,cols)

    def T(self): #returns matrix transpose
        T =  [ self[i] if type(self[i]) == complex else self[i] for i in range(len(self))]
        return Vector(T, is_row=not self.is_row)

    def H(self): #complex conjugate equivalent of the tranpose
        H = [ conj(self[i]) if type(self[i]) == complex else self[i] for i in range(len(self)) ]
        return Vector(H,is_row= not self.is_row)

    def __getitem__(self,index):
        if type(index) == int:
            column_index = index*int(self.is_row == True) + 0*int(self.is_row != True)
            row_index = 0*int(self.is_row == True) + index*int(self.is_row != True)
            return self.matrix[row_index][column_index]
        elif type(index) == slice:
            if self.is_row:
                return Vector(self.matrix[0][index])
            else:
                return Vector(self.matrix[index])
        
    def __setitem__(self,index,item):

        if type(index)==tuple:
                
            y,x = index

            if type(item) == Vector:
                
                i_n = len(item)
                if item.is_row: #it's a row vector
                    start = int(0 if x.start == None else x.start)
                    end = int(len(self[0]) if x.stop == None else x.stop)+1
                    if type(y) != int:
                        raise Exception("Operation failed: Item dimensions too large, it is row vector, so cannot span multipe rows")
                else:
                    start = int(0 if y.start == None else y.start)
                    end = int(len(self) if y.stop == None else y.stop)+1
                    if type(x) != int:
                        raise Exception("Operation failed: Item dimensions too large, it is column vector, so cannot span multipe columns")

                if i_n != (end-start):
                    raise Exception("Operation failed: Item change dimensions do not match, check the what you are trying to change")
                
                if item.is_row: #again, row vector
                    for j in range(start,end):
                        self.matrix[0][j] = item[j-start]
                else:
                    for j in range(start,end):
                        self.matrix[j][0] = item[j-start]
                

            elif type(item) in numbers.__args__:
                
                if type(x) != int or type(y) != int:
                    raise Exception("Input size does not match")
                
                self.matrix[y][x] = item
            
            else:
                raise Exception("Set operation failed: Input type is not compatible with Vector")
        
        else:
            
            if self.is_row: #is row vector
                self.matrix[0][index] = item
            else:
                self.matrix[index][0] = item

    def __len__(self):
        return len(self.matrix)*int(self.is_row != True) + len(self.matrix[0])*int(self.is_row == True)
    
    def __add__(self,B): # addition

        if type(B) == Vector and len(self) == len(B) and self.is_row == B.is_row:
            C = [ self[i]+B[i] for i in range(len(B)) ]
            return Vector(C,is_row=self.is_row)
        else:
            raise Exception("Vector dimensions or types don't match! (Addition)")
    
    def __sub__(self,s): #subdivision

        if type(s) != Vector or self.is_row != s.is_row or len(self) != len(s):
            raise Exception("Vector dimensions or types do not match! (Subtraction)")

        S = Vector([ 0 for _ in range(len(self)) ],is_row=self.is_row)
        for i in range(len(self)):
                S[i] = self[i] - s[i]
        return S
    
    def __mul__(self,v):
        
        if type(v) in numbers.__args__: #allows element wise moltiplication by scalar with the matrix
            Z = Vector([ v*self[j] for j in range()],is_row=self.is_row)
            return Vector(Z)

        [rows,columns] = self.size()

        if columns != v.size()[0]:
            raise Exception("Operation failed (Vector): Dimensions are not compatible to multiplication.")

        new_columns = v.size()[1]
        Z = Matrix([[ 0 for _ in range(new_columns)] for _ in range(rows)])
        
        for i in range(new_columns):
            for j in range(rows):
                sum = 0
                for k in range(columns):
                    sum += self.matrix[j][k] * v.matrix[k][i]
                Z[j,i] = sum
        
        if [rows,new_columns] == [1,1]:
            return Z[0]
        else:
            return Z
        

    def __truediv__(self,s): #element-wise division
        S = [self[i]/s  for i in range(len(self)) ]
        return Vector(S,is_row=self.is_row)

    def __pow__(self,b):
        
        if type(b) == int or type(b) == float:
            I = []
            for j in range(len(self)-1):
                I.append(self[j] ** b)
            return Vector(I,is_row=self.is_row)
        
        # matmul didn't work for some reason I just chose to repurpose the power operator to permit element-wise matrix multiplication
        # this will be useful when discretizing for non-linear analysis and solving ODEs
        elif isinstance(b,ndarray):
            if self.size() != b.size():
                raise Exception("Dimensions do not match for element-wise multiplication")
            
            [rows,cols] = self.size()
            P = []
            for j in range(rows):
                for i in range(cols):
                    P.append(self[j][i] * b[j][i])
            return Vector(P,self.is_row)

    def col(self): #function to make vectors columns

        if self.is_row: #matrix is row vector, need to return column vector
            return self.T()
        else: #it's a column vector, no change is needed
            return self   

    def row(self): #function to make vectors columns

        if self.is_row: #matrix is column vector, need to return row vector
            return self
        else: #it's a row vector, no change is needed
            return self.T()
        
    def sum(self):
        rows = len(self)
        s = 0
        try:
            for j in range(rows):
                s += self[j]
            return s
        except:
            return s
        
    def size(self):
        #Returns [row,colu]
        if not self.is_row:
            return [len(self.matrix),1]
        return [1,len(self.matrix[0])]































def conj(integer:numbers):
    return complex(integer.real,-1*integer.imag)