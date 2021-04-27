# Python3 Program to decompose
# a matrix into lower and
# upper traingular matrix

import numpy as np

 
 
def luDecomposition(mat, n):
 
    lower = [[0 for x in range(n)]
             for y in range(n)]
    upper = [[0 for x in range(n)]
             for y in range(n)]
 
    # Decomposing matrix into Upper
    # and Lower triangular matrix
    for i in range(n):
 
        # U
        for k in range(i, n):
 
            # Summation of L(i, j) * U(j, k)
            sum = 0
            for j in range(i):
                sum += (lower[i][j] * upper[j][k])
 
            # Evaluating U(i, k)
            upper[i][k] = mat[i][k] - sum
 
        # L
        for k in range(i, n):
            if (i == k):
                lower[i][i] = 1  # Diagonal as 1
            else:
 
                # Summation of L(k, j) * U(j, i)
                sum = 0
                for j in range(i):
                    sum += (lower[k][j] * upper[j][i])
 
                # Evaluating L(k, i)
                lower[k][i] = int((mat[k][i] - sum) /
                                  upper[i][i])
 
    # setw is for displaying nicely
    print("L:\t\t\t\tU:")
 
    # Displaying the result :
    for i in range(n):
 
        # Lower
        for j in range(n):
            print(lower[i][j], end="\t")
        print("", end="\t")
 
        # Upper
        for j in range(n):
            print(upper[i][j], end="\t")
        print("")

    return lower, upper
 
 
# Driver code
mat = [[2, -1, -2],
       [-4, 6, 3],
       [-4, -2, 8]]

b = [1, 1, 1]
n=len(b)
 
L, U=luDecomposition(mat, n)

y=[0]*n
x=[0]*n
A=mat
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


