"""After # ----------- # do not touch anything"""
"""Here is the text to be deciphered"""
word = 'clayton prepared we and odor we run night to reduce cross or multiply to will proceed the will at sweet where be on langford hounds clayton owl bailed hickory hermes add the the tree of the'
word = word.split()

"""Here is the key to be encrypted"""
key = '-1 3 -2 6 5 -4'
key = key.split()

"""number of columns"""
column = len(key)

"""number of columns"""
row = 7

"""words that change"""
dict_ = {'hounds': 'batteries', 'odor': 'Vicksburg', 'clayton': 'April', 'sweet': '16', 'tree': 'Grand', 'owl': 'Gulf',
         'bailed': 'forts.', 'hickory': 'river', 'multiply': '25', 'add': '29.', 'hermes': 'Admiral',
         'langford': 'Porter.'}
#----------------------------------------------------------------------------------------------------------------------#
list_ = []
matrix_text = []
text = ''

x = 0
result_text = ''
for i in range(column):
    list_.append(word[x:x + 6])
    x += 6

numbers = 0
for x in range(column):
    matrix_text.append([])
for ke in key:
    if int(ke) < 0:
        matrix_text[abs(int(ke)) - 1] = list_[numbers][::-1]
    else:
        matrix_text[int(ke) - 1] = list_[numbers]
    numbers += 1

for x in range(column):
    for i in range(row - 1):
        text += matrix_text[i][x] + " "

for te in text.split():
    if te in dict_:
        result_text += dict_[te] + ' '
    else:
        result_text += te + ' '
"""outputs the result"""
print(result_text)
