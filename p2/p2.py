import numpy as np
import scipy as sp
import math 

def readMatrix(path):
    completPath = 'p2/matrix/' + path
    M = np.loadtxt(completPath,"f")
    return M

def readVector(path):
    completePath = 'p2/vector/' + path
    vector = np.loadtxt(completePath)
    return vector

def traspuesta(M):
    dim = len(M)
    Mt = np.zeros((dim,dim),"f")
    for i in range(dim):
        for j in range(dim):
            Mt[i,j] = M[j,i]
    return Mt

def richardsonMethod(A,b,x0,maxIter,maxErr):
    k = 0
    x = x0
    alpha = 0.2
    #error = .0
    while (k<maxIter):
        k+=1
        r = b - np.dot(A,x)
        x = x + alpha*r
    print k   
    return x

def optimGradient(A,b,x0,maxIter,maxErr):
    k = 0
    x = x0
    #error = .0
    while (k<maxIter):
        k+=1
        r = b - np.dot(A,x)
        alpha = np.dot(r,r) / np.dot(np.transpose(r),np.dot(A,r)) 
        x = x + alpha*r
    print k   
    return x

def conjGradient(A,b,x0,maxIter,maxErr):
    k = 0
    x = x0
    r = b-np.dot(A,x)
    p = r
    #error = .0
    while (k<maxIter):
        k+=1
        alpha = np.dot(r,r) / np.dot(np.transpose(p),np.dot(A,p)) 
        x = x + alpha*p
        r0 = r
        r = r - alpha * np.dot(A,p)
        beta = np.dot(r,r) / np.dot(r0,r0)
        p = r +  beta*p
    
    print k   
    return x


if __name__ == '__main__':
    A = readMatrix('xmatrix.txt')
    xvector = readVector('xvector.txt')
    print richardsonMethod(A,xvector,[0,0,0],5,0)
    print optimGradient(A,xvector,[0,0,0],8,0)
    print conjGradient(A,xvector,[0,0,0],2,0)