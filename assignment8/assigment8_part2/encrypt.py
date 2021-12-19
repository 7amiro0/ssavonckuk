"""After # ----------- # do not touch anything"""
"""Here is the text to be encrypted"""
text = '''We will run the batteries at Vicksburg the night of April 16 and proceed to Grand Gulf
          where we will reduce the forts. Be prepared to cross the river on April 25 or 29. Admiral Porter.'''
words = text.split()

"""Here is the key to be encrypted"""
key = '-1 3 -2 6 5 -4'
key = key.split()

"""number of columns"""
column = len(key)

"""number of columns"""
row = 7

"""words that change"""
dict = {'batteries': 'hounds', 'Vicksburg': 'odor', 'April': 'clayton', '16': 'sweet', 'Grand': 'tree', 'Gulf': 'owl',
        'forts.': 'bailed', 'river': 'hickory', '25': 'multiply', '29.': 'add', 'Admiral': 'hermes',
        'Porter.': 'langford'}
#----------------------------------------------------------------------------------------------------------------------#
list_ = []
text = []
result_text = ''

for number in range(row):
    height = word[number::column]
    list_.append(height)

for ke in key:
    if int(ke) < 0:
        text += list_[abs(int(ke)) - 1][::-1]
    elif int(ke) > 0:
        text += list_[abs(int(ke)) - 1]

for te in text:
    if te in dict:
        result_text += dict[te] + ' '
    else:
        result_text += te + ' '

"""outputs the result"""
print(result_text.lower())
