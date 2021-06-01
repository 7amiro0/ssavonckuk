word = 'THIS OFF DETAINED ASCERTAIN WAYLAND CORRESPONDENTS OF AT WHY AND IF FILLS IT YOU GET THEY NEPTUNE THE TRIBUNE PLEASE ARE THEM CAN UP'
word = word.split()
open_text = 'correspondents of the Tribune wayland at neptune please ascertain why they are detained and get them off if you can this fills it up'

key = [[-1, 2], [1, -2], [-2, 1], [2, -1]]

column = 2
row = 12
list_ = []
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
    text = []
    result_text = ''
    for k in ke:
        if k < 0:
            text.append(list_[abs(k) - 1][::-1])
        else:
            text.append(list_[abs(k) - 1])


    for i in range(row):
        result_text += text[0][i] + ' '
        result_text += text[1][i] + ' '

    print(result_text.lower(), ke)

key = [[-1, 2, -3], [1, -2, 3], [3, -2, 1], [-3, 2, -1]]

column = 3
row = 8
list_ = []
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
    text = []
    result_text = ''
    for k in ke:
        if k < 0:
            text.append(list_[abs(k) - 1][::-1])
        else:
            text.append(list_[abs(k) - 1])


    for i in range(row):
        result_text += text[0][i] + ' '
        result_text += text[1][i] + ' '
        result_text += text[2][i] + ' '

    print(result_text.lower(), ke)
key = [[-1, 2, -3, 4], [1, -2, 3, -4], [-4, 3, -2, 1], [4, -3, 2, -1]]

if len(key) == 0 or len(word) == 0:
    input('Pleas pres enter of exit program')
    exit()

column = 4
row = 6
list_ = []
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
    text = []
    result_text = ''
    for k in ke:
        if k < 0:
            text.append(list_[abs(k) - 1][::-1])
        else:
            text.append(list_[abs(k) - 1])


    for i in range(row):
        result_text += text[0][i] + ' '
        result_text += text[1][i] + ' '
        result_text += text[2][i] + ' '
        result_text += text[3][i] + ' '

    print(result_text.lower(), ke)

key = [[-1, 2, -3, 4, -5, 6], [1, -2, 3, -4, 5, -6], [-6, 5, -4, 3, -2, 1], [6, -5, 4, -3, 2, -1]]

column = 6
row = 4
list_ = []
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
    text = []
    result_text = ''
    for k in ke:
        if k < 0:
            text.append(list_[abs(k) - 1][::-1])
        else:
            text.append(list_[abs(k) - 1])


    for i in range(row):
        result_text += text[0][i] + ' '
        result_text += text[1][i] + ' '
        result_text += text[2][i] + ' '
        result_text += text[3][i] + ' '


    print(result_text.lower(), ke)

key = [[-1, 2, -3, 4, -5, 6, -7, 8], [1, -2, 3, -4, 5, -6, 7, -8], [-8, 7, -6, 5, -4, 3, -2, 1], [8, -7, 6, -5, 4, -3, 2, -1]]

column = 8
row = 3
list_ = []
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
    text = []
    result_text = ''
    for k in ke:
        if k < 0:
            text.append(list_[abs(k) - 1][::-1])
        else:
            text.append(list_[abs(k) - 1])


    for i in range(row):
        result_text += text[0][i] + ' '
        result_text += text[1][i] + ' '
        result_text += text[2][i] + ' '
        result_text += text[3][i] + ' '


    print(result_text.lower(), ke)

key = [[-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11, 12], [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12], [-12, -11, -10, 9, -8, 7, -6, 5, -4, 3, -2, 1], [12, -11, 10, -9, 8, -7, 6, -5, 4, -3, 2, -1]]

column = 12
row = 2
list_ = []
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
    text = []
    result_text = ''
    for k in ke:
        if k < 0:
            text.append(list_[abs(k) - 1][::-1])
        else:
            text.append(list_[abs(k) - 1])


    for i in range(row):
        result_text += text[0][i] + ' '
        result_text += text[1][i] + ' '
        result_text += text[2][i] + ' '
        result_text += text[3][i] + ' '


    print(result_text.lower(), ke)