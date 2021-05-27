"""home works 5."""
choice = input('choice 1 or 2, 1 = encrypt 2 =  decrypt: ')

if choice == '1':
    word = input('enter your message: ')
    word = word.split()
    key = input('enter your key: ')
    key = key.split()

    if len(key) == 0 or len(word) == 0:
        input('Pleas pres enter of exit program')
        exit()

    column = 4
    row = 4
    list_ = []
    text = []
    result_text = ''

    for i in range(column):
        list_.append([])
    for w in range(len(word)):
        list_[w % row].append(word[w])
    for ke in key:
        if int(ke) < 0 and list_[abs(int(ke)) - 1] not in text:
            text += list_[abs(int(ke)) - 1][::-1]
        elif int(ke) > 0 and list_[abs(int(ke)) - 1] not in text:
            text += list_[abs(int(ke)) - 1]

    for te in text:
        result_text += te + ' '

    print(result_text)

elif choice == "2":

    word = input('enter your message: ')
    word = word.split()
    key = input('enter your key: ')
    key = key.split()

    if len(key) == 0 or len(word) == 0:
        input('Pleas pres enter of exit program')
        exit()

    column = 4
    row = 4
    list_ = []
    text = []
    result_text = ''
    x = 0

    for i in range(column):
        list_.append([])
    for w in range(len(word)):
        if len(list_[x]) != 5:
            list_[x].append(word[w])
        else:
            x += 1
            list_[x].append(word[w])

    for ke in key:
        if int(ke) < 0 and list_[abs(int(ke)) - 1] not in text:
            text.append(list_[abs(int(ke)) - 1][::-1])
        elif int(ke) > 0 and list_[abs(int(ke)) - 1] not in text:
            text.append(list_[abs(int(ke)) - 1])

    print(text)

    for i in range(5):
        result_text += text[0][i] + ' '
        result_text += text[1][i] + ' '
        result_text += text[2][i] + ' '
        result_text += text[3][i] + ' '
    print(result_text)
