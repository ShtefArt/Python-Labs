
e = float(input("Enter e = "))
x = float(input("Enter x = "))
i = 1
a_n = (4 / 5) * x + x / (5 * pow(x, 4))
a_n_1 = a_n + 2*e
while i < 100 and abs(a_n - a_n_1) > e:
    a_n_1 = a_n
    a_n = (4 / 5) * a_n_1 + x / (5 * pow(a_n_1, 4))
    i += 1
print("Number = ", i - 1)
print("First element = ", a_n)





