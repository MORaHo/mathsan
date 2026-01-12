import sys
from typing import Union

numbers = Union[int, float, complex]

##---------------##
#| NDARRAY CLASS |#
##---------------##

COLUMN_MAJOR = 0
ROW_MAJOR = 1


## Functions used in __str__ to convert from i to an index to print the intended matrix entry
row_str_lambda = lambda i,rows,columns: i
col_str_lambda = lambda i,rows,columns: (i%columns)*rows+(i//columns)

class ndarray:

    def __init__(self, data, size:list[int]=[],major:int=ROW_MAJOR,transpose_flag:bool=False,preserve_flag:bool=False):

        """
            data: Is the list of data entries which will be the base for our array, which we will have to parse to clear needs
            size: List of given dimensions for the array, if it empty we look at the shape of the given data, and if the data is of type list[int], we consider it a vector
            major: Direction in which we store data (row major order or column major order), different orientations have their distinct advantages
            preserve_flag: Logical flag to make sure data is not accidentaly transposed, indicates whether the data already follows the major which is indicated.
        """

        if type(data) in numbers.__args__:
            self.matrix = [data]
            self.size = [1,1]

        if len(size) != 0: #we don't check type since size has been declared so the data will either match what is given in size or it is of type list[int]

            element = data[0]
            data_depth = 1

            while type(element) not in numbers.__args__:
                data_depth += 1
                element = element[0]

            if data_depth > 2 or len(size) > 2:
                raise Exception("Arrays with dimension greater than 2, currently not supported!")

            if data_depth > 1 and len(size) != data_depth:
                raise Exception("Data input size not equal to size input!")

            data_size = 1
            for s in size:
                data_size *= s

            if data_depth == 1 and data_size != len(data):
                raise Exception("Data input entry not equal to input size dimension!")
            elif data_depth == 2 and data_size != len(data)*len(data[0]):
                raise Exception("Data input entry not equal to input size dimension!")

            if data_depth == 1:
                self.matrix = data
                if len(size) == 1:
                    self.matrix = data
                    self.size = [1,size[0]] #default to row vector
                else:
                    if transpose_flag is False: #If a column major order is called for, we organize data in such a manner. preserve_flag tells us if the vectorialized data is already
                        # ordered as the major is indicating.
                        if major == ROW_MAJOR or preserve_flag is True:
                            self.matrix == data
                        else: #because we default to believing it's a row major
                            [rows,columns] = size
                            self.matrix = []
                            for i in range(len(data)): #this can probably be collapsed inside the self.matrix declaration, but keeping for now for legibility.
                                row = i%rows
                                column = i//rows
                                entry = row*columns+column
                                self.matrix.append(data[entry])
                    elif transpose_flag is True:
                        if preserve_flag == True:
                            [rows,columns] = size
                            self.matrix = []
                            for i in range(len(data)): #this can probably be collapsed inside the self.matrix declaration, but keeping for now for legibility.
                                row = i%columns
                                column = i//columns
                                entry = row*rows+column
                                self.matrix.append(data[entry])
                            size = size[::-1]
                        else:
                            self.matrix = data
                            size = size[::-1]
                    self.size = size


                if self.size[0] != 1 and self.size[1] == 1: #if the size indicates that it is a column vector, change the default setting
                    major = COLUMN_MAJOR
                elif self.size[0] == 1 and self.size[1] != 1:
                    major = ROW_MAJOR

            elif data_depth == 2:
                if major == COLUMN_MAJOR: #We don't need preserve_flag here because Python matrices are already naturally row ordered, so independent of that
                    # we will have to convert it to column major ordered.
                    self.matrix = []
                    for i in range(len(data[0])):
                        for j in range(len(data)):
                            self.matrix.append(data[j][i])
                else:
                    self.matrix = []
                    for i in range(len(data[0])):
                        for j in range(len(data)):
                            self.matrix.append(data[j][i])
                self.size = size
            else: #this is currenly not supported so it is just here to take space and add a not
                # To be able to vectorizalise tensors of larger dimensions that one, I will need to recursively iterate through
                # the data, but since I am currently limiting myself to vectors and matricies, this will currently be left unused.
                pass

        elif len(size) == 0: #in this case the data is either pre-formatted or it will be treated as a vector so we already know that is of type list[int]

            # we don't use preserve_flag at any point here, because how vectors are stored doesn't change based on order direction, and input of type list[list]
            # will only be external, so all internal operations will be treated by the above code.

            if type(data[0]) is int: #it's a vector
                if major: #if it's a row vector (default)
                    self.size = [1,len(data)]
                else:
                    self.size = [len(data),1]
                self.matrix = data

            else:
                size = [len(data),len(data[0])]
                element = data[0][0]
                while type(element) not in numbers.__args__:
                    size.append(len(element))
                    element = element[0]

                if len(size) > 2:
                    raise Exception("Matrices with dimension greater than 2 are currently not able to be generated!")
                if major != ROW_MAJOR: #generate a column-major ordered flattened array
                    self.matrix = []
                    [_,columns] = size
                    for i in range(len(data)):
                        row = i//columns
                        column = i % columns
                        self.matrix.append(data[row][column])
                else:
                    self.matrix = []
                    for i in range(len(data)):
                        self.matrix += data[i]
                self.size = size

        else:
            self.matrix = []
            self.size = [0,0]
            print("Notice: Whether intentional or due to error, empty matrix has been generated!")

        self.major = major

    def len(self):
        return len(self.matrix)

    def T(self):  # returns matrix transpose
        major = COLUMN_MAJOR * int(self.major == ROW_MAJOR) + ROW_MAJOR * int(self.major != ROW_MAJOR)
        return Matrix(data=self.matrix,size=self.size,major=major,transpose_flag = True,preserve_flag = False)
        # preserve_flag is false, since the __init__ does not know that we are transposing that data, so when we go to do another operation like __add__
        # and the array which we are inputting has self.major = COLUMN_MAJOR, and we want to keep this, __init__ will not know that the data is already in
        # column major order (since by default we are treating all matrices as row major ordered) and will unintentially transpose the data, so preserve_flag
        # is there to prevent this behaviour.

    def H(self):  # complex conjugate equivalent of the tranpose
        major = COLUMN_MAJOR * int(self.major == ROW_MAJOR) + ROW_MAJOR * int(self.major != ROW_MAJOR)
        H = [ conj(self.matrix[j]) if type(self.matrix[j]) is complex else self.matrix[j] for j in range(self.len()) ]
        return Matrix(H,size=self.size,major=major,transpose_flag = True, preserve_flag = False)

    def __str__(self):
        """Prints matrix in Matlab style, although the variable name is not printed"""
        string = "\n"
        [rows,columns] = self.size
        if self.major == ROW_MAJOR:
            str_function = row_str_lambda
        else:
            str_function = col_str_lambda
        for i in range(self.len()):
            string += "  "
            index = str_function(i,rows,columns)
            entry = self.matrix[index]
            if type(entry) is complex:
                real = format(float(entry.real), ".3")
                cmplx = format(float(entry.imag), ".3")
                string += str(real)
                string += "+"
                string += str(cmplx)
                string += "j"
                string += "  "
            else:
                number = format(float(entry),'.4')
                string += str(number)
                string += "  "
            if (i+1)%(columns)==0 and i>0:
                string += "\n"
        return string

    def __len__(self):
        return len(self.matrix)

    def __getitem__(self, index):

        [rows,columns] = self.size

        if self.major == ROW_MAJOR:
            if type(index) is int:
                return self.matrix[columns*index:columns*(index+1)]

            elif type(index) is slice:
                y_start = int(0 if index.start is None else index.start)
                y_end = int(rows if index.stop is None else index.stop)
                return self.matrix[y_start*columns:y_end*columns]

            try:
                if type(index) is tuple and len(index) == 2:
                    y, x = index

                    if type(y) is slice:
                        y_start = int(0 if y.start is None else y.start)
                        y_end = int(rows if y.stop is None else y.stop)
                    elif type(y) is int:
                        y_start = y
                        y_end = y + 1
                    if type(x) is slice:
                        x_start = int(0 if x.start is None else x.start)
                        x_end = int(columns if x.stop is None else x.stop)
                    elif type(x) is int:
                        x_start = x
                        x_end = x + 1

                    M = [ self.matrix[j*columns+x_start:j*columns+x_end] for j in range(y_start, y_end) ]

                    rows = y_end-y_start
                    cols = x_end-x_start

                    if [rows, cols] != [1, 1]:

                        return Matrix(M,size=[rows,cols],major=self.major,preserve_flag=True)
                    else:
                        return M[0][0]

            except:
                return []

        else: #column ordered array, returns
            if type(index) is int:
                return self.matrix[index:columns*rows+index:rows]

            elif type(index) is slice:
                y_start = int(0 if index.start is None else index.start)
                y_end = int(rows if index.stop is None else index.stop)
                return [self.matrix[i:(columns-1)*rows+i:rows] for i in range(y_start,y_end)]

            try:
                if type(index) is tuple and len(index) == 2:
                    y, x = index

                    if type(y) is slice:
                        y_start = int(0 if y.start is None else y.start)
                        y_end = int(rows if y.stop is None else y.stop)
                    elif type(y) is int:
                        y_start = y
                        y_end = y + 1
                    if type(x) is slice:
                        x_start = int(0 if x.start is None else x.start)
                        x_end = int(columns if x.stop is None else x.stop)
                    elif type(x) is int:
                        x_start = x
                        x_end = x + 1
                    M = [ self.matrix[ x_start*rows+i:x_end*rows+i:rows ] for i in range(y_start, y_end) ]

                    if [len(M), len(M[0])] != [1, 1]:
                        return Matrix(M,major=self.major,preserve_flag=True)
                    else:
                        return M[0][0]

            except:
                return []


    def __add__(self, item):  #This function is a candidate for parallelizations since no operation is dependent on other operations.

        if type(self) is not type(item) or self.size != item.size:
            raise Exception("Matrix dimensions or types don't match for addition!")

        C = []
        [rows,columns] = self.size

        selfrowstep = columns*int(self.major == ROW_MAJOR) + 1*int(self.major != ROW_MAJOR)
        selfcolstep = 1*int(self.major == ROW_MAJOR) + rows*int(self.major != ROW_MAJOR)
        itemrowstep = columns*int(item.major == ROW_MAJOR) + 1*int(item.major != ROW_MAJOR)
        itemcolstep = 1*int(item.major == ROW_MAJOR) + rows*int(item.major != ROW_MAJOR)

        for i in range(len(self.matrix)):
            row = i // columns
            column = i % columns

            k = row * selfrowstep + column * selfcolstep
            j = itemrowstep * row + itemcolstep * column

            C.append(self.matrix[k] + item.matrix[j])

        return Matrix(data=C,size=self.size,major=self.major,preserve_flag=True)

    def __sub__(self, item):  # subdivision

        if type(self) is not type(item) or self.size != item.size:
            raise Exception("Matrix dimensions or types don't match for addition!")

        C = []
        [rows,columns] = self.size

        selfrowstep = columns*int(self.major == ROW_MAJOR) + 1*int(self.major != ROW_MAJOR)
        selfcolstep = 1*int(self.major == ROW_MAJOR) + rows*int(self.major != ROW_MAJOR)
        itemrowstep = columns*int(item.major == ROW_MAJOR) + 1*int(item.major != ROW_MAJOR)
        itemcolstep = 1*int(item.major == ROW_MAJOR) + rows*int(item.major != ROW_MAJOR)

        for i in range(len(self.matrix)):
            row = i // columns
            column = i % columns

            k = row * selfrowstep + column * selfcolstep
            j = itemrowstep * row + itemcolstep * column

            C.append(self.matrix[k] - item.matrix[j])

        return Matrix(data=C,size=self.size,major=self.major,preserve_flag=True)

    def __truediv__(self, s):  # element-wise division
        S = [self.matrix[i] / s for i in range(len(self.matrix))]
        return Matrix(S,size=self.size,major=self.major,preserve_flag=True)

##--------------##
#| MATRIX CLASS |#
##--------------##

class Matrix(ndarray):

    def __new__(cls, data, size:list[int] = [0,0],major:int=ROW_MAJOR,transpose_flag:bool=False,preserve_flag:bool=False):
        [rows,columns] = size
        if rows < 2 or columns < 2:
            if columns == 0 and len(data) == 1:  # it's a row
                return Vector(data,axis=ROW_MAJOR)
            try:
                if len(data[0]) == 1:
                    return Vector(data,axis=COLUMN_MAJOR)
                else:
                    return super(Matrix, cls).__new__(cls)
            except:
                return Vector(data,axis=COLUMN_MAJOR)

        else:
            return super(Matrix, cls).__new__(cls)

    def __init__(self, data,size:list[int]=[0,0] , major:int=ROW_MAJOR , transpose_flag:bool=False , preserve_flag:bool=False):
        [rows,columns] = size
        rows = rows * (rows != 0) + len(data) * (rows == 0)
        try:
            columns = columns * (columns != 0) + len(data[0]) * (columns == 0)
        except:
            columns = columns
        size = [rows,columns]
        if type(data) is list and type(data[0]) is list:
            size = []
        super().__init__(data=data,size=size,major=major,transpose_flag=transpose_flag,preserve_flag=preserve_flag)


    def __setitem__(self, index, item):

        [rows,cols] = self.size
        if type(index) is tuple and len(index) == 2:
            y, x = index

            if type(item) is Matrix:

                item_rows, item_columns = item.size

                if type(y) is slice and type(x) is slice:
                    y_start = int(0 if y.start is None else y.start)
                    y_end = int(rows if y.stop is None else y.stop)
                    x_start = int(0 if x.start is None else x.start)
                    x_end = int(cols if x.stop is None else x.stop)

                    [rows,cols] = self.size

                    if item_columns != x_end-x_start or item_rows != y_end-y_start:
                        raise Exception("Input error: Input dimensions do not match slice area!")

                    if y_end > rows or x_end > cols or x_start < 0 or y_start < 0:
                        raise Exception("Input error: Slice bounds outside of matrix")


                    itemdenom = 1*int(item.major == ROW_MAJOR) + item_columns*int(item.major != ROW_MAJOR)
                    itemstep = 1*int(item.major == ROW_MAJOR) + item_rows*int(item.major != ROW_MAJOR)
                    offsetstepy = cols*int(self.major == ROW_MAJOR) + 1*int(self.major != ROW_MAJOR)
                    offsetstepx = 1*int(self.major == ROW_MAJOR) + rows*int(self.major != ROW_MAJOR)

                    itemsize = item_rows*item_columns

                    for k in range(itemsize):
                        itemrow = k//itemdenom
                        itemcol = k%itemdenom
                        itemi = itemrow + itemcol * itemstep
                        #We first have to find the position in the matrix without the offset
                        subrow = (k // item_columns)
                        subcol = k % item_columns
                        subi =  (subrow + subcol * rows)*int(self.major != ROW_MAJOR) + (subrow * rows + subcol)*int(self.major == ROW_MAJOR)
                        # Then we can find the position in the matrix after applying the offset
                        i = subi + y_start*offsetstepy + x_start*offsetstepx
                        self.matrix[i] = item.matrix[itemi]


            elif type(item) is Vector:

                [rows,columns] = self.size

                item_length = len(item)

                if item.major == ROW_MAJOR:  # it's a row vector
                    start = int(0 if x.start is None else x.start)
                    end = int(columns if x.stop is None else x.stop)
                    if type(y) is not int:
                        raise Exception("Item dimensions too large, it is row vector, so cannot span multipe rows!")
                else:
                    start = int(0 if y.start is None else y.start)
                    end = int(rows if y.stop is None else y.stop)
                    if type(x) is not int:
                        raise Exception("Item dimensions too large, it is column vector, so cannot span multipe columns!")

                if item_length != (end - start):
                    raise Exception("Input vector and given dimensions do not match, check the what you are trying to change!")

                if item.major == ROW_MAJOR:  # again, row vector
                    col = cols*int(self.major == ROW_MAJOR) + 1*int(self.major != ROW_MAJOR)
                    row = 1*int(self.major == ROW_MAJOR) + rows*int(self.major != ROW_MAJOR)
                    step = 1*int(self.major == ROW_MAJOR) + rows*int(self.major != ROW_MAJOR)
                    shift = y * col + start * row
                else:
                    col = 1*int(self.major == ROW_MAJOR) + rows*int(self.major != ROW_MAJOR)
                    row = cols*int(self.major == ROW_MAJOR) + 1*int(self.major != ROW_MAJOR)
                    step = cols*int(self.major == ROW_MAJOR) + 1*int(self.major != ROW_MAJOR)
                    shift = x * col + start * row
                for i in range(len(item)):
                    k = step * i + shift
                    self.matrix[k] = item.matrix[i]

            elif type(item) in numbers.__args__:

                if type(x) is not int or type(y) is not int:
                    raise Exception("Input size does not match, input is int,float or complex, so slice dimensions should be 1 and 1!")
                [rows,columns] = self.size
                row_step = cols*int(self.major == ROW_MAJOR) + 1*int(self.major != ROW_MAJOR)
                col_step = 1*int(self.major == ROW_MAJOR) + rows*int(self.major != ROW_MAJOR)
                self.matrix[y*row_step+x*col_step] = item
        elif type(index) is slice:

            if isinstance(item, ndarray):

                [rows,cols] = self.size
                [itemrows,itemcols] = item.size
                start = index.start
                end = index.stop
                if itemcols != cols or itemrows != end-start:
                    raise Exception("Number of columns in input does not match matrix columns!")

                denom = 1*int(self.major == ROW_MAJOR) + cols*int(self.major != ROW_MAJOR)
                step = 1*int(self.major == ROW_MAJOR) + rows*int(self.major != ROW_MAJOR)
                itemdenom = 1*int(item.major == ROW_MAJOR) + itemcols*int(item.major != ROW_MAJOR)
                itemstep = 1*int(item.major == ROW_MAJOR) + itemrows*int(item.major != ROW_MAJOR)
                offsetstep = cols*int(self.major == ROW_MAJOR) + 1*int(self.major != ROW_MAJOR)

                itemsize = itemrows*itemcols
                for k in range(itemsize):
                    itemcol = k%itemdenom
                    itemrow = k//itemdenom
                    itemi = itemrow + itemcol * itemstep
                    row = k % denom
                    col = k // denom
                    i = col + (row) * step + start*offsetstep
                    self.matrix[i] = item.matrix[itemi]

            elif type(item) is list and type(item[0]) is list:

                [rows,cols] = self.size
                [itemrows,itemcols] = [len(item),len(item[0])]
                start = index.start
                end = index.stop

                if itemcols != cols or itemrows != end-start:
                    raise Exception("Number of columns in input does not match matrix columns!")

                denom = 1*int(self.major == ROW_MAJOR) + cols*int(self.major != ROW_MAJOR)
                step = 1*int(self.major == ROW_MAJOR) + rows*int(self.major != ROW_MAJOR)
                offsetstep = cols*int(self.major == ROW_MAJOR) + 1*int(self.major != ROW_MAJOR)

                itemsize = itemrows*itemcols
                for k in range(itemsize):
                    itemrow = k//itemcols
                    itemcol = k%itemcols
                    row = k // denom
                    col = k % denom
                    i = row + (col) * step + start*offsetstep
                    self.matrix[i] = item[itemrow][itemcol]

            else:
                start = index.start
                end = index.stop
                raise Exception("Input error: For setting into slice, input must have same dimensions are area sliced! In this case: "+str(end-start)+" x "+str(self.size[1]))
        elif type(index) is int:
            if type(item) is not list and type(item) is not Vector:
                raise Exception("Input should be a list or vector")
            if type(item) is Vector and item.major != ROW_MAJOR:
                raise Exception("Input should be row vector, currently not!")
            [rows,columns] = self.size
            if len(item) != columns:
                raise Exception("Dimension does not match number of columns in matrix!")
            step = 1*int(self.major == ROW_MAJOR) + rows*int(self.major != ROW_MAJOR)
            row = columns*int(self.major == ROW_MAJOR) + 1*int(self.major != ROW_MAJOR)
            if type(item) is list:
                for i in range(columns):
                    k = index*row + i*step
                    self.matrix[k] = item[i]
            elif type(item) is Vector:
                for i in range(columns):
                    k = index*row + i*step
                    self.matrix[k] = item.matrix[i]
        else:
            if type(item) is not list or len(item) is not len(self[index]):
                raise Exception("Input size does not match required size by matrix!")
            self[index] = item

    def __mul__(self, item):  # element-wise scalar multiplication and dot product
        [rows, columns] = self.size  # rows,columns

        if type(item) in numbers.__args__:# allows element wise moltiplication by scalar with the matrix
            Z = [item * self.matrix[j] for j in range(len(self.matrix))]

            return Matrix(Z,size=self.size,major=self.major,preserve_flag = True)

        elif columns != item.size[0]:# if the dimensions don't match the dotproduct cannot be performed
            raise Exception("Dimensions of the two matrices don't match")

        [item_rows,item_columns] = item.size
        Z = []

        rowstep = columns*int(self.major == ROW_MAJOR) + 1*int(self.major != ROW_MAJOR)
        colstep = 1*int(item.major == ROW_MAJOR) + item_rows*int(item.major != ROW_MAJOR)
        j_selfstep = 1*int(self.major == ROW_MAJOR) + rows*int(self.major != ROW_MAJOR)
        j_itemstep = item_columns*int(item.major == ROW_MAJOR) + 1*int(item.major != ROW_MAJOR)

        for i in range(item_columns*rows):

            matrow = i // item_columns #Because we are finding the row in the matrix we are generating, which has the same number of columns as the multiplicand.
            matcol = i % item_columns
            sum = 0

            for j in range(columns): #could also be item_rows as it would be the same
                k = matrow * rowstep + j * j_selfstep
                itemi = matcol * colstep + j * j_itemstep
                sum += self.matrix[k]*item.matrix[itemi]
            Z.append(sum)

        if [rows, item_columns] == [1, 1]:
            return Z[0]
        else:
            return Matrix(Z,size=[rows,item_columns],major=ROW_MAJOR)

    def __rmul__(self, m):
        if type(m) in numbers.__args__:
            R = []
            for i in range(len(self)):
                R.append(m*self.matrix[i])
            return Matrix(R,size=self.size,major = self.major, preserve_flag=True)
        else:
            return self.__mul__(m)

    def __pow__(self, item):
        if type(item) is int or type(item) is float:
            I = [self.matrix[i]*item for i in range(len(self.matrix))]
            return Matrix(I, size=self.size,major=self.major,preserve_flag=True)

        # matmul didn't work for some reason I just chose to repurpose the power operator to permit element-wise matrix multiplication
        # this will be useful when discretizing for non-linear analysis and solving ODEs
        elif isinstance(item, ndarray):

            if self.size != item.size:
                raise Exception("Dimensions do not match for element-wise multiplication")

            [rows, cols] = self.size

            selfrowstep = cols*int(self.major == ROW_MAJOR) + 1*int(self.major != ROW_MAJOR)
            selfcolstep = 1*int(self.major == ROW_MAJOR) + rows*int(self.major != ROW_MAJOR)
            itemrowstep = cols*int(item.major == ROW_MAJOR) + 1*int(item.major != ROW_MAJOR)
            itemcolstep = 1*int(item.major == ROW_MAJOR) + rows*int(item.major != ROW_MAJOR)

            P = []

            for i in range(len(self.matrix)):

                row = i // cols
                col = i % cols
                k = row * selfrowstep + col * selfcolstep
                j = row * itemrowstep + col * itemcolstep

                P.append(self.matrix[k] * item.matrix[j])

            return Matrix(P,size=self.size,major=ROW_MAJOR)


##--------------##
#| VECTOR CLASS |#
##--------------##


class Vector(ndarray):

    def __init__(self, data,axis:int=COLUMN_MAJOR,transpose_flag:bool=False,preserve_flag:bool=False):
        if axis==ROW_MAJOR and type(data[0]) is not list:
            rows = 1
            cols = len(data)
            super().__init__(data,size=[rows,cols],major=axis,transpose_flag=transpose_flag,preserve_flag=preserve_flag)
        elif len(data) == 1 and type(data[0]) is list:
            axis  = ROW_MAJOR
            rows = 1
            cols = len(data[0])
            super().__init__(data,size=[rows,cols],major=axis,transpose_flag=transpose_flag,preserve_flag=preserve_flag)
        elif len(data) == 1:
            axis  = ROW_MAJOR
            rows = 1
            cols = 1
            super().__init__(data,size=[rows,cols],major=axis,transpose_flag=transpose_flag,preserve_flag=preserve_flag)
        else:
            axis = COLUMN_MAJOR
            rows = len(data)
            cols = 1
            super().__init__(data,size=[rows,cols],major=axis,transpose_flag=transpose_flag,preserve_flag=preserve_flag)

    def T(self):  # returns matrix transpose
        return Vector(self.matrix,axis=self.major,transpose_flag=True)

    def H(self):  # complex conjugate equivalent of the tranpose
        H = [ conj(self.matrix[j]) if type(self.matrix[j]) is complex else self.matrix[j] for j in range(self.len()) ]
        return Vector(H,axis=self.major,transpose_flag = True)

    def __getitem__(self, index):
        if type(index) == int:
            return self.matrix[index]
        elif type(index) == slice:
            return Vector(self.matrix[index],axis=self.major)

    def __setitem__(self, index, item):

        [rows,_] = self.size

        if type(index) is slice:

            start = int(0 if index.start is None else index.start)
            end = int(rows if index.stop is None else index.stop)

            if type(item) is Vector or type(item) is list:
                item_length = len(item)
                if item_length != (end - start):
                    raise Exception("Operation failed: Item change dimensions do not match, check the what you are trying to change")

                for j in range(start, end):
                    self.matrix[j] = item[j - start]

            else:
                raise Exception("Set operation failed: Input type is not compatible with Vector")

        elif type(index) is int:
            if type(item) is list and len(item) == 1:
                self.matrix[index] = item[0]
            elif type(item) not in numbers.__args__:
                raise Exception("Set operation failed: Input has to be int,float or complex")
            else:
                self.matrix[index] = item #operation is independent of major order

        else:
            raise Exception("Operation failed: Index type invalid!")

    def __str__(self):
        string = "\n"
        for i in range(self.len()):
            string += "  "
            entry = self.matrix[i]
            if type(entry) is complex:
                real = format(float(entry.real), ".3")
                cmplx = format(float(entry.imag), ".3")
                string += str(real)
                string += "+"
                string += str(cmplx)
                string += "j"
                string += "  "
            else:
                number = format(float(entry),'.4')
                string += str(number)
                string += " "
            if self.major == COLUMN_MAJOR and i<len(self.matrix):
                string += "\n"
        return string

    def __add__(self, B):  # addition
        if type(B) is not Vector or self.size != B.size or self.major != B.major:
            raise Exception("Vector dimensions or types don't match! (Addition)")
        return Vector([self[i] + B[i] for i in range(len(self.matrix))],axis = self.major)

    def __sub__(self, s):  # subdivision
        if type(s) is not Vector or self.major != s.major or self.size != s.size:
            raise Exception("Vector dimensions or types do not match! (Subtraction)")
        return Vector([self.matrix[i]-s[i] for i in range(len(self.matrix))], axis=self.major)

    def __mul__(self, v):

        if type(v) in numbers.__args__:  # allows element wise moltiplication by scalar with the matrix
            return  Vector([v * self[j] for j in range(len(self.matrix))], axis=self.major)

        if len(self) != len(v) or self.major == v.major:
            raise Exception("Operation failed (Vector): Dimensions are not compatible to multiplication.")

        if self.major != ROW_MAJOR:
            V = []
            length = len(self)
            for i in range(length): #using two for loops in this case I think is best since it avoids calculating mult every iteration.
                mult = self[i]
                for j in range(length):
                    V.append(mult*v[j])
            return Matrix(V,size=[length,length])

        else: #only two possible cases, so insteading of writing one since operation, I wrote two
            sum = 0
            for i in range(len(self)):
                sum += self[i]*v[i]
            return sum

    def __pow__(self, b):
        if type(b) is int or type(b) is float:
            I = [self.matrix[j] ** b for j in range(len(self.matrix) - 1)]
            return Vector(I, axis=self.major)

        # matmul didn't work for some reason I just chose to repurpose the power operator to permit element-wise matrix multiplication
        # this will be useful when discretizing for non-linear analysis and solving ODEs
        elif isinstance(b, ndarray):
            if self.size != b.size or self.major != b.major:
                raise Exception("Dimensions do not match for element-wise multiplication")
            P = [self[i]*b[i] for i in range(len(self.matrix))]
            return Vector(P, axis=self.major)

    def col(self):  # function to make vectors columns
        if self.major == ROW_MAJOR:  # matrix is row vector, need to return column vector
            return self.T()
        return self

    def row(self):  # function to make vectors columns
        if self.major == ROW_MAJOR:  # matrix is column vector, need to return row vector
            return self
        return self.T()

    def sum(self):
        sum = 0
        for i in range(len(self.matrix)):
            sum += self.matrix[i]
        return sum


def conj(integer: numbers):
    return complex(integer.real, -1 * integer.imag)
