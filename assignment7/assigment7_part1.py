"""After # ----------- # do not touch anything"""
"""Here we have a message that can be changed __
                                                |
                                                V"""
word = 'THIS OFF DETAINED ASCERTAIN WAYLAND CORRESPONDENTS OF AT WHY AND IF FILLS IT YOU GET THEY NEPTUNE THE TRIBUNE PLEASE ARE THEM CAN UP'
word = word.split()
#----------------------------------------------------------------------------------------------------------------------#
"""Here we pick up the keys"""
for c in range(2, len(word)):
    if len(word) % c == 0:
        COLUMN = c
        key = []
        for r in range(len(word)):
            if COLUMN * r == len(word):
                ROW = r
                rever = -1
                l = []
                q = []
                for k in range(1, COLUMN + 1):
                    rever = -rever
                    l.append(k * rever)
                    q.append(k * -rever)

                b = l[::-1]
                c = q[::-1]
                key.append(l)
                key.append(q)
                key.append(b)
                key.append(c)
                list_ = []
                x = 0
                """here everything is laid out in columns"""
                for i in range(COLUMN):
                    list_.append([])
                for w in range(len(word)):
                    if len(list_[x]) != ROW:
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

                    for i in range(ROW):
                        for c in range(COLUMN - 1):
                            result_text += text[c][i] + ' '
                    """here the output and keys are output"""
                    print(result_text.lower(), ke)
