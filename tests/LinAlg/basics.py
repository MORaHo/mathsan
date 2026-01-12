import sys
from src.LinAlg.utils import isequal
from src.LinAlg.ndarray import Matrix,Vector

### This file implements tests to see if all the functionalities in LinAlg.matrix function or not, since without them nothing else will work

def alert(message:str):
    print(message)
    sys.exit()

## Matrix generation test

matrix = [1,1,1,1,1,1,1,1,1]
A = Matrix([[1,1,1],[1,1,1],[1,1,1]])
A_ = Matrix([1,1,1,1,1,1,1,1,1],size=[3,3])
tests_passed = 0

if A.matrix != matrix or A_.matrix != matrix:
    print(A.matrix)
    alert("Major error: Matrix generation not working!")

x = Vector([1,1,1,1,1])
vector_matrix = [1,1,1,1,1]

if x.matrix != vector_matrix:
    alert("Vector not generating properly")

tests_passed += 1

## Type-setting test

# These test if the code properly generates a Vector in the special cases we have called upon the matrix generation
x = Matrix([1,1,1,1,1])
vector_matrix = [1,1,1,1,1]
row = Matrix([[1,1,1,1,1]])
row_matrix = [1,1,1,1,1]

if x.matrix != vector_matrix or row.matrix != row_matrix:
    alert("Vector not generating properly from Matrix call")

## __setitem__ test

A1 = Matrix([[1,1,1],[1,1,1],[1,1,1]])
B = Vector([2,2])
C1 = Matrix([[1,1,1],[2,1,1],[2,1,1]])
A1[1:3,0] = B

A2 = Matrix([[1,1,1],[1,1,1],[1,1,1]])
B = Matrix([[2,2],[2,2]])
A2[1:,1:] = B
C2 = Matrix([[1,1,1],[1,2,2],[1,2,2]])

if not isequal(A1,C1) or not isequal(A2,C2):
    alert("Set item not working")

tests_passed += 1

## Transpose test

A = Matrix([[1,2,3],[4,5,6],[7,8,9]])
T = Matrix([[1,4,7],[2,5,8],[3,6,9]])

if not isequal(A.T(),T):
    alert("Transpose matrix generation method not working!")

tests_passed += 1

if len(A) != 9:
    alert("len(A) not working!")

tests_passed += 1

A = Matrix([[1,2,3],[4,5,6],[7,8,9]])
B = Matrix([[1,1,1],[1,1,1],[1,1,1]])
C = A + B
D = Matrix([[2,3,4],[5,6,7],[8,9,10]])
if not isequal(C,D):
    alert("Sum method not working! (general case)")

tests_passed += 1

E = Matrix([[1,2,3],[4,5,6]])

try:
    E + D
    #if this works as it should "Matrix dimensions or types don't match", which is what should happen as they do not effectively match
    alert("Sum method not working, adding matrices of different sizes!")
except:
    tests_passed += 1

C = A - B
D = Matrix([[0,1,2],[3,4,5],[6,7,8]])

if not isequal(C,D):
    alert("Subtraction method not working")

A = Matrix([[1,2,3],[4,5,6],[7,8,9]])
alpha = 2.5
B = alpha * A
C = Matrix([[2.5,5,7.5],[10,12.5,15],[17.5,20,22.5]])
x = Vector([1,2,3])
y = Vector([14,32,50])
D = Matrix([[1,2,3],[2,4,6],[3,6,9]])

if not isequal(B,C):
    alert("Integer-matrix multiplication sub-method not working")

if not isequal(A*x,y) or not isequal(x*x.T(),D) or x.T()*x != 14:
    alert("Matrix-vector multiplication not working")

A *= x
x *= x.T()

if not isequal(A,y) or not isequal(x,D):
    alert("rmul not working") #this only limited to the first two cases

A = Matrix([[1,2,3],[4,5,6],[7,8,9]])
B = A/2
C = Matrix([[1/2,2/2,3/2],[4/2,5/2,6/2],[7/2,8/2,9/2]])

if not isequal(B,C):
    alert("Division not working")

## Element-wise multiplication test, this type of multiplication is needed in non-linear analysis to find the y values of a given funciton
A = Matrix([[1,2,3],[4,5,6],[7,8,9]])
B = Matrix([[2,3,4],[5,6,7],[8,9,10]])
C = Matrix([[2,6,12],[20,30,42],[56,72,90]])

#if not isequal(A**B,C):
#    alert("Element-wise multiplication not working")

A = Matrix([[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]])
B = Matrix([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]])

if A.size != [3,5] or B.size != [5,4]:
    alert("Size method not working!")

x = Vector([1,1,1,1,1])
y = Vector([1,1,1,1,1],axis=1)


if not isequal(x.row(),y) or not isequal(y.col(),x):
    alert("Row or column methods not working!")

print("All tests passed!")
