import numpy as np
import scipy as sp
import math 
def choleskyFactoring(A):
    dim = len(A)
    L = np.zeros((dim,dim),"f")
    for i in range(dim):
        for j in range( i + 1):
            sumatory = sum(L[i,k]*L[j,k] for k in range(dim))

            if i == j:
                L[i,i] = math.sqrt (A[j,j] - sumatory)
            else:
                L[i,j] = 1 / L[j,j] * (A[i,j] - sumatory) 
    return L
                
def solveEcuation():
    pass

def readInput(path):
    M = np.loadtxt(path,"f")
    return M
def writeOutput(path):
    pass

if __name__ == '__main__':
    A = readInput('p1/xmatrix.txt')
    C = choleskyFactoring(A)
    S = np.linalg.cholesky(A)

    print('Solucion Cholesky \n' + str(S))
    print('Mi solucion \n '+str(C))
    

    