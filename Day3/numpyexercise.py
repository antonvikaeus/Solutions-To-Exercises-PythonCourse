#!/usr/bin/env python

import numpy as np
#a
v1 = np.zeros(10)
v1[4] = 1
print(v1)
#b
v2 = np.arange(10,50)
print(v2)
#c
v3 = v2[::-1]
print(v3)
#d
v4 = np.arange(9).reshape(3,3)
print  (v4)
#e
v5 = np.array([1,2,0,0,4,0])
v55 = np.where(v5 != 0)[0]
print(v55)
#f
v6 = np.random.random(30)
v66 = np.mean(v6)
print(v66)
#g
v7 = np.zeros(49).reshape(7,7)
v7[[0,-1],:]=1
v7[:,[0,-1]]=1
print(v7)
#h
v8 = np.zeros(64).reshape(8,8)
even = slice(0,8,2) ; odd = slice(1,9,2) ;
v8[even,odd]=1; v8[odd,even]=1 ;
print(v8)
#i
#for x in range((dim)):
#    i = np.append(i,[np.tile(t,int(dim))])
#i = np.array(i).reshape(8,8)
#print(i)
#or
v9 = np.tile(np.array([[0,1],[1,0]]),(4,4))
print(v9)
#j
Zj = np.array([0,1,2,3,4,5,6,7,8,9,10])
Zj[range(3,8)] = -Zj[range(3,8)]
print(Zj)
#k
Zk = np.random.random(10)
Zk = np.sort(Zk)
print(Zk)

#l
A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)
equal = (A==B)
print(equal)

#m
Zm = np.arange(10, dtype=np.int32)
print(Zm.dtype)
Zm = np.float32(Zm)
print(Zm.dtype)

#n
A = np.arange(9).reshape(3,3)
B = A + 1
C = np.dot(A,B)
print(C)
D = np.diag(C)
print(D)