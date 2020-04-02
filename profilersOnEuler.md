30397485
Timer unit: 1e-06 s

Total time: 0.003736 s
File: ./euler72.py
Function: gen_primes at line 12

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    12                                           @profile
    13                                           def gen_primes(n):
    14         1          7.0      7.0      0.2      l = range(2,n)
    15         1          0.0      0.0      0.0      primes = []
    16       999        234.0      0.2      6.3      for j in range(0,len(l)):
    17       998        212.0      0.2      5.7          p = True
    18      2968        783.0      0.3     21.0          for d in primes:
    19      2967        947.0      0.3     25.3              if(d > sqrt(l[j])):
    20       167         41.0      0.2      1.1                  break
    21      2800        830.0      0.3     22.2              if(l[j] % d == 0):
    22       830        197.0      0.2      5.3                  p = False
    23       830        190.0      0.2      5.1                  break;
    24       998        226.0      0.2      6.0          if(p):
    25       168         69.0      0.4      1.8              primes.append(l[j])
    26                                           
    27         1          0.0      0.0      0.0      return primes

Total time: 0.101043 s
File: ./euler72.py
Function: factorize at line 29

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    29                                           @profile
    30                                           def factorize(n,primes):
    31      9999       2264.0      0.2      2.2      factors = []
    32      9999       1919.0      0.2      1.9      init_n = n
    33     96347      19311.0      0.2     19.1      for p in primes:
    34    118736      31266.0      0.3     30.9          while(n%p == 0):
    35     22389       5671.0      0.3      5.6              n = n/p
    36     22389       6254.0      0.3      6.2              factors.append(p)
    37     96347      25394.0      0.3     25.1          if(p > sqrt(n)):
    38      9999       2015.0      0.2      2.0              break
    39      9999       2205.0      0.2      2.2      if(n > 1):
    40      9596       2781.0      0.3      2.8          factors.append(n)
    41      9999       1963.0      0.2      1.9      return factors

Total time: 0.217685 s
File: ./euler72.py
Function: fast_phi at line 58

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    58                                           @profile
    59                                           def fast_phi(n,primes):
    60      9999     188950.0     18.9     86.8      factors = factorize(n,primes)
    61      9999       2824.0      0.3      1.3      phi = factors[0]-1
    62     31985       9994.0      0.3      4.6      for i in range(1,len(factors)):
    63     21986       6655.0      0.3      3.1          if(factors[i] == factors[i-1]):
    64      7685       3147.0      0.4      1.4              phi *= (factors[i]-1)*(factors[i])/(factors[i]-1)
    65                                                   else:
    66     14301       4137.0      0.3      1.9              phi *= (factors[i]-1)
    67      9999       1978.0      0.2      0.9      return phi



The factorization on line 60 is the most time consuming operation. Therefore, put speedoptimization here.

Regarding memory, each line takes up even amounts of memory. However some of the functions have more executions which sum up to more overall memory in a single function.

Below is an example of the memory used by euler72.py
Line #    Mem usage    Increment   Line Contents
================================================
    58   27.973 MiB   27.973 MiB   @profile
    59                             def fast_phi(n,primes):
    60   27.973 MiB   27.973 MiB       factors = factorize(n,primes)
    61   27.973 MiB    0.000 MiB       phi = factors[0]-1
    62   27.973 MiB    0.000 MiB       for i in range(1,len(factors)):
    63   27.973 MiB    0.000 MiB           if(factors[i] == factors[i-1]):
    64   27.973 MiB    0.000 MiB               phi *= (factors[i]-1)*(factors[i])/(factors[i]-1)
    65                                     else:
    66   27.973 MiB    0.000 MiB               phi *= (factors[i]-1)
    67   27.973 MiB    0.000 MiB       return phi
