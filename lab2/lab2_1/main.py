import numpy as np

def count_T(k):
    if k == 1:
        return x
    elif k == 0:
        return 1
    else:
        return (2 * x * count_T(k - 1)) - count_T(k - 2)

def input_arr(Y):
    print("Enter Y: ")
    i = 0
    while i < n:
        Y[i] = input()
        i += 1

def count_sum(Y):
    res = 0
    for i in range(0, n):
        res += (pow((-1) * Y[i], i)) * count_T(i)
    return res



x = float(input("Enter x: "))
n = int(input("Enter n: "))
y = np.zeros(n, float)
input_arr(y)
print(count_sum(y))