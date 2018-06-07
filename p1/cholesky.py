from numpy import array, zeros, matrix, linalg, dot, loadtxt, random,ones
import scipy as sp
import math 
def choleskyFactoring(A):
    dim = len(A)
    L = zeros((dim,dim),"f")

    return L
                
def solveEcuation():
    pass

def readInput(path):
    M = loadtxt(path)
    return M
def writeOutput(path):
    pass

if __name__ == '__main__':
    A = readInput('p1/xmatrix.txt')
    C = choleskyFactoring(A)
    S = linalg.cholesky(A)

    print('Solucion Cholesky \n' + str(S))
    print('Mi solucion \n '+str(C))
    

    