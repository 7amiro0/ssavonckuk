"""home works 5."""
choice = input('choice 1 or 2, 1 = encrypt 2 =  decrypt: ')

if choice == '1':
    word = input('enter your message: ')
    word = word.split()
    key = input('enter your key: ')
    key = key.split(",")

    column = 5
    list_ = []
    text = []

    for i in range(column):
        list_.append([])
    for w in range(len(word)):
        list_[w % column].append(word[w])
    for ke in key:
        if int(ke) < 0 and list_[abs(int(ke)) - 1] not in text:
            text += list_[abs(int(ke)) - 1][::-1]
        elif int(ke) > 0 and list_[abs(int(ke)) - 1] not in text:
            text += list_[abs(int(ke)) - 1]

    print(text)
elif choice == "2":

    word = input('enter your secret message: ')
    word = word.split()
    key = input('enter your key: ')
    key = key.split(",")

    column = 5
    list_ = []
    text = []
    result_text = ''

    for i in range(column):
        list_.append([])
    for w in range(len(word)):
        list_[w % column].append(word[w])

    for ke in key:
        if int(ke) < 0 and list_[abs(int(ke)) - 1] not in text:
            text += list_[abs(int(ke)) - 1][::-1]
        elif int(ke) > 0 and list_[abs(int(ke)) - 1] not in text:
            text += list_[abs(int(ke)) - 1]

    for i in range(len(word)):
        result += text[i] + ' '

    print(result)
