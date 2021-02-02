import numpy as np


A = np.arange(0,24).reshape(4,6)
print("Original matrix")
print(A)

def rota90(mat):
    print(np.rot90(mat))
print("90 matrix")
rota90(A)

def rota180(mat):
    print(np.rot90(mat,2))
print("180 matrix")
rota180(A)

def rota270(mat):
    print(np.rot90(mat,3))
print("270 matrix")
rota270(A)

#######


def rota90_(mat):
    print(np.rot90(mat,1,(1,0)))
print("-90 matrix")
rota90_(A)

def rota180_(mat):
    print(np.rot90(mat,2,(1,0)))
print("-180 matrix")
rota180_(A)

def rota270_(mat):
    print(np.rot90(mat,3,(1,0)))
print("-270 matrix")
rota270_(A)

