word = 'txt word init hello bro nine four samir nikita artem roma andrey lox'
a = 0
win = []
list1 = []
list2 = []
list3 = []
list4 = ['1', '2', '3', '4', '5']
for w in word.split():
    if len(list1) < 5:
        list1.append(w)
        continue
    elif len(list1) == 5 and len(list2) != 5:
        list2.append(w)
        continue
    elif len(list2) == 5 and len(list3) != 5:
        list3.append(w)
        continue
for z in list1:
    win.append(z)
    continue
for x in list2:
    win.append(x)
    continue
for c in list3:
    win.append(c)
    continue
for v in list4:
    win.append(v)
    continue
print(win)

