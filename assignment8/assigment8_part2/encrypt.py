word = 'We will run the batteries at Vicksburg the night of April 16 and proceed to Grand Gulf where we will reduce the forts. Be prepared to cross the river on April 25 or 29. Admiral Porter.'
word = word.split()
key = '-1 3 -2 6 5 -4'
key = key.split()

fail_list = []
column = 6
row = 6
list_ = []
text = []
result_text = ''
dict = {'batteries': 'hound', 'Vicksburg': 'odor', 'April': 'clayton', '16': 'sweet', 'Grand': 'tree', 'Gulf': 'owl',
        'forts.': 'bailed', 'river': 'hickory', '25': 'multiply', '29.': 'add', 'Admiral': 'hermes',
        'Porter.': 'langford'}
failed_word = 'dog cat human veligers time day'
failed_word = failed_word.split()

for i in range(column):
    list_.append([])
for w in range(len(word)):
    list_[w % row].append(word[w])

for x in range(column):
    list_[x].append(failed_word[x])

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

print(result_text.lower())
