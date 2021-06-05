word = 'we multiply to will proceed the will the of tree the the add run will or cross reduce to night run we odor and we prepared clayton at at sweet where be on langford hound the hermes hickory bailed owl clayton hound'
word = word.split()
key = '-1 3 -2 6 5 -4'
key = key.split()

column = 6
row = 7
list_ = []
text = []
result_text = ''
dict_ = {'hound': 'batteries', 'odor': 'Vicksburg', 'clayton': 'April', 'sweet': '16', 'tree': 'Grand', 'owl': 'Gulf', 'bailed': 'forts.', 'hickory': 'river', 'multiply': '25', 'add': '29.', 'hermes': 'Admiral', 'langford': 'Porter.'}
x = 0

for i in range(column):
    list_.append([])
for w in range(len(word)):
    if len(list_[x]) != row:
        list_[x].append(word[w])
    else:
        x += 1
        list_[x].append(word[w])

for ke in key:
    if int(ke) < 0:
        text += list_[abs(int(ke)) - 1][::-1]
    elif int(ke) > 0:
        text += list_[abs(int(ke)) - 1]

for te in text:
    if te in dict_:
        result_text += dict_[te] + ' '
    else:
        result_text += te + ' '

print(result_text.lower())
