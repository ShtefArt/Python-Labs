str = input("Enter string: ")
words = str.split()
words_dict = {}
word = ''
while words:
    word = words.pop()
    if words_dict.get(word) == None:
        words_dict[word] = 0
    else:
        words_dict[word] = words_dict.get(word) + 1
max = 0
word = ''
for key, value in words_dict.items():
    if value > max:
        max = value
        word = key
    elif value == max:
        if key < word:
            word = key

print(word)
