word = 'THIS OFF DETAINED ASCERTAIN WAYLAND CORRESPONDENTS OF AT WHY AND IF FILLS IT YOU GET THEY NEPTUNE THE TRIBUNE PLEASE ARE THEM CAN UP'
word = word.split()
open_text = 'correspondents of the Tribune wayland at neptune please ascertain why they are detained and get them off if you can this fills it up'
for c in range(2, 12):
    if len(word) % c == 0:
        COLUMN = c
        key = []
        for r in range(2, 12):
            if COLUMN * r == len(word):
                ROW = r
                rever = -1
                l = []
                q = []
                for k in range(1, COLUMN):
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

                    print(result_text.lower(), ke)
