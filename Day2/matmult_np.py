#!/usr/bin/python

# Program to multiply two matrices using nested loops


'''import line_profiler
import atexit
profile = line_profiler.LineProfiler()
atexit.register(profile.print_stats)
'''
import random
import numpy as np

N=250

@profile
# NxN matrix
def Xmat(N):
    X = []
    for i in range(N):
        X.append([random.randint(0,100) for r in range(N)])
    return X

@profile
# Nx(N+1) matrix
def Ymat(N):    
    Y = []
    for i in range(N):
        Y.append([random.randint(0,100) for r in range(N+1)])
    return Y

@profile
# result is Nx(N+1)
def Rmat(N):
    result = []
    for i in range(N):
        result.append([0] * (N+1))
    return result

@profile
# iterate through rows of X
def matrixmultiplication(X,Y,result):
    for i in range(len(X)):
        # iterate through columns of Y
        for j in range(len(Y[0])):
            result[i][j] = np.dot(X[i] , Y[:,j])
    


X = Xmat(N) 
Y = Ymat(N)
result = Rmat(N)
    
np_X = np.array(X)
np_Y = np.array(Y)
np_result = np.array(result)

matrixmultiplication(np_X,np_Y,np_result)


#Not necessesary to print
#for r in result:
 #   print(r)
