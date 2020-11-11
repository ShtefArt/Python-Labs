import re

string = input("Enter string: ")
i = 0
j = 0
l = 0
res_i = 0
res_j = 0
tem_j = 0
tem_i = 0
count = 0
temp_count = 0
str_arr = re.split("[., :;?!]", string)
for str in str_arr:
    if str == '':
        j += 1
for j in range(0, j):
    str_arr.remove('')
for str in str_arr:
    if str != '':
        if len(str) == l:
            count += 1
            if temp_count < count:
                temp_count = count
                res_i = i
                res_j = tem_j
        elif len(str) != l:
            if temp_count < count:
                temp_count = count
                res_j = tem_j
                res_i = tem_i
            l = len(str)
            count = 1
            tem_j = i
        tem_i = i
    i += 1
print(', '.join(str_arr[res_j:res_i + 1]))


