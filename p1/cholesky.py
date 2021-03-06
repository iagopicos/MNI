import numpy as np
import scipy as sp
import math 

def traspuesta(M):
    dim = len(M)
    Mt = np.zeros((dim,dim),"f")
    for i in range(dim):
        for j in range(dim):
            Mt[i,j] = M[j,i]
    return Mt

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
          
def solveCholesky(A):
  pass

def gaussSeidel(A,vector,iter,tol,error):
    dimI = len(A)
    dimJ = len(A[0])
    x = np.zeros(len(vector),"f")
    k = 0 
    while k<iter:
        sum = 0
        k+=1
        for i in range(dimI):
            sum = 0
            for j in range (dimJ):
                if (i != j): #Comprobamos que no estamos en la diagonal
                    sum = sum + A[i,j] * x[j]
            x[i] = (vector[i] - sum) / A[i,i]
        
    return x

def methodSOR(A,vector,aproximation,maxIter,maxError,omega):
    dimI = len(A)
    dimJ = len(A[0])
    #if aproximation == None:
    x = np.zeros(dimJ,"f")
    #x = aproximation
    iter = 0 
    error = 0
    
    while (iter<maxIter):
        sum = 0
        iter+=1
        for i in range(dimI):
            sum = 0
            
            for j in range (dimJ):
                if (i != j): #Comprobamos que no estamos en la diagonal
                    sum = sum + A[i,j] * x[j] #Preparo la suma de las componentes para luego calcular xi correspondiente
            anterior = x[i]
            x[i] =  x[i] *(1-omega) +( (vector[i] - sum) * omega / A[i,i])
            error = abs((x[i] - anterior) / x[i])
        if error < maxError:
                print 'Convergencia alcanzada'
                break
            
    print('Numero de iteraciones: '+str(iter))
    print('Error final:'+ str(error))    
    return x



def readMatrix(path):
    completPath = 'p1/matrix/' + path
    M = np.loadtxt(completPath,"f")
    return M

def readVector(path):
    completePath = 'p1/vector/' + path
    vector = np.loadtxt(completePath)
    return vector

def writeSolution(path):
    pass

if __name__ == '__main__':
    A = readMatrix('xmatrix.txt')
    vector = readVector('xvector.txt')
    
    #print vector
    x = methodSOR(A,vector,None,20,0.002,0.6)
    #(A,vector,aproximation,maxIter,maxError,omega)
    print x
    