

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
while i <= len(string):

    if i == len(string):
        if i - j != l:
            if temp_count < count:
                temp_count = count
                res_j = tem_j
                res_i = tem_i
            break
        elif i - j == l:
            count += 1
            if temp_count < count:
                temp_count = count
                res_i = i
                res_j = tem_j
            break
    if string[i] == "," or string[i] == ' ' or string[i] == '.' or string[i] == ';' or string[i] == ':' or string[i] == '?' or string[i] == '!':
        count += 1

        if i - j != l:
            if temp_count < count - 1:
                temp_count = count - 1
                res_j = tem_j
                res_i = j - 1
            l = i - j
            count = 1
            tem_j = j

        tem_i = i
        while i < len(string) and (string[i] == "," or string[i] == ' ' or string[i] == '.' or string[i] == ';' or string[i] == ':' or string[i] == '?' or string[i] == '!'):
            i += 1
        j = i
    i += 1
if temp_count < count:
    res_i = i - 1
    res_j = tem_j
print(string[res_j: res_i])

