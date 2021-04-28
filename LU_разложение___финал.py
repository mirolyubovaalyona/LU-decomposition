# Python3 Program to decompose
# a matrix into L and
# U traingular matrix

import numpy as np

 
 
def luDecomposition(mat, n):
 
    L = np.zeros((n,n))
    U = mat
 

    for i in range(n):
        for j in range(i, n):
            L[j][i]=U[j][i]/U[i][i]
    for k in range(1, n):
        for i in range(k-1, n):
             for j in range(i, n):
                 L[j][i]=U[j][i]/U[i][i]
        for i in range(k, n):
             for j in range(k-1, n):
                 U[i][j]=U[i][j]-L[i][k-1]*U[k-1][j]
                

    print("L:\t\t\t\tU:")
    print(L)
    print(U)
    

    return L, U
 
 

n = int(input('Количество неизвестных: '))

a = np.zeros((n,n))
b = np.zeros(n)

for i in range(n):
    for j in range(n):
        a[i][j] = float(input( 'a['+str(i)+']['+ str(j)+']='))

for i in range(n):
        b[i] = float(input( 'b['+str(i)+']='))
 
L, U=luDecomposition(a, n)

y=[0]*n
x=[0]*n
A=a
for i in range(n):
    alpha = 0;
    for k in range(0, i):
        alpha  += L[i][k]*y[k]
    y[i] = b[i] - alpha


for i in range(n-1, -1, -1):
    alpha = 0
    for k in range(i+1, n):
        alpha  += U[i][k]*x[k]
    x[i] = (1 / U[i][ i]) * (y[i] - alpha)

print("x:")
for i in range(n):
    print("x", i, "=", x[i])


