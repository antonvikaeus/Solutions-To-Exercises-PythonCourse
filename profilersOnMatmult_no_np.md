Running the line profiler:

Timer unit: 1e-06 s

Total time: 0.15685 s
File: ./matmult.py
Function: Xmat at line 16

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    16                                           @profile
    17                                           # NxN matrix
    18                                           def Xmat(N):
    19         1          1.0      1.0      0.0      X = []
    20       251         66.0      0.3      0.0      for i in range(N):
    21     62750     156783.0      2.5    100.0          X.append([random.randint(0,100) for r in range(N)])
    22         1          0.0      0.0      0.0      return X

Total time: 0.149585 s
File: ./matmult.py
Function: Ymat at line 24

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    24                                           @profile
    25                                           # Nx(N+1) matrix
    26                                           def Ymat(N):    
    27         1          1.0      1.0      0.0      Y = []
    28       251         65.0      0.3      0.0      for i in range(N):
    29     63000     149519.0      2.4    100.0          Y.append([random.randint(0,100) for r in range(N+1)])
    30         1          0.0      0.0      0.0      return Y

Total time: 0.000913 s
File: ./matmult.py
Function: Rmat at line 32

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    32                                           @profile
    33                                           # result is Nx(N+1)
    34                                           def Rmat(N):
    35         1          0.0      0.0      0.0      result = []
    36       251         47.0      0.2      5.1      for i in range(N):
    37       250        866.0      3.5     94.9          result.append([0] * (N+1))
    38         1          0.0      0.0      0.0      return result

Total time: 8.3186 s
File: ./matmult.py
Function: matrixmultiplication at line 40

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    40                                           @profile
    41                                           # iterate through rows of X
    42                                           def matrixmultiplication(X,Y,result):
    43       251        120.0      0.5      0.0      for i in range(len(X)):
    44                                                   # iterate through columns of Y
    45     63000      13207.0      0.2      0.2          for j in range(len(Y[0])):
    46                                                       # iterate through rows of Y
    47  15750250    3111279.0      0.2     37.4              for k in range(len(Y)):
    48  15687500    5193996.0      0.3     62.4                  result[i][j] += X[i][k] * Y[k][j]


Clearly, the most time consuming operation is the for loop and the construction of the result matrix.
Therefore speed optimization should be put in line 47 and 48.

Furthermore the appending of values to the Xmatrix and Ymatrix take some time. So there optimization could do well.


Improving the matrix multiplication by using numpy gave about a 85 % decrease in time consumed for the matrix multiplication. Below is the line profile output.

Total time: 0.117364 s
File: ./matmult_np.py
Function: matrixmultiplication at line 40

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    40                                           @profile
    41                                           # iterate through rows of X
    42                                           def matrixmultiplication(X,Y,result):
    43       251         60.0      0.2      0.1      for i in range(len(X)):
    44                                                   # iterate through columns of Y
    45     63000      14619.0      0.2     12.5          for j in range(len(Y[0])):
    46     62750     102685.0      1.6     87.5              result[i][j] = np.dot(X[i] , Y[:,j])


Running the memory profiler:

Memory usage on the matrix mult gives:
Filename: matmult_np.py

Line #    Mem usage    Increment   Line Contents
================================================
    40   42.008 MiB   42.008 MiB   @profile
    41                             # iterate through rows of X
    42                             def matrixmultiplication(X,Y,result):
    43   42.008 MiB    0.000 MiB       for i in range(len(X)):
    44                                     # iterate through columns of Y
    45   42.008 MiB    0.000 MiB           for j in range(len(Y[0])):
    46   42.008 MiB    0.000 MiB               result[i][j] = np.dot(X[i] , Y[:,j])

Where we see that we use 42 MiB each on lines 45 and 46

while running this on the original matmult script we acquire

Filename: matmult.py

Line #    Mem usage    Increment   Line Contents
================================================
    40   29.289 MiB   29.289 MiB   @profile
    41                             # iterate through rows of X
    42                             def matrixmultiplication(X,Y,result):
    43   30.047 MiB    0.000 MiB       for i in range(len(X)):
    44                                     # iterate through columns of Y
    45   30.047 MiB    0.000 MiB           for j in range(len(Y[0])):
    46                                         # iterate through rows of Y
    47   30.047 MiB    0.258 MiB               for k in range(len(Y)):
    48   30.047 MiB    0.000 MiB                   result[i][j] += X[i][k] * Y[k][j]

Lines 47 48 once again use the most memory, this time less than when using numpy.