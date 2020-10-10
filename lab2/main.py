import numpy as np

def input_arr(A):
    i = 0
    j = 0
    while i < n:
        print("Row:", i)
        while j < n:
            A[i, j] = input()
            j += 1
        j = 0
        i += 1

def row_check(a):
    i = 0
    if n%2 == 0:
        while i < n/2:
            if a[i] != a[n - i - 1]:
                return False
            i += 1
    else:
        while i < (n + 1)/2:
            if a[i] != a[n - i - 1]:
                return False
            i += 1
    return True

def build_vector(A, B):
    i = 0
    k = 0
    while i < n:
        if row_check(A[i]) == True:
            B[k] = i
            k += 1
        i += 1
    B.resize(k, refcheck=False)

def print_vector(B):
    i = 0
    while i < B.size and i < 7:
        print(B[i], end=" ")
        i += 1
    while i < B.size and i < 14:
        print(B[i], end=" ")
        i += 1
    while i < B.size:
        print(B[i], end=" ")
        i += 1

n = int(input("Enter n: "))
a = np.zeros((n, n), int)
b = np.zeros(n, int)
input_arr(a)
build_vector(a, b)
print_vector(b)
