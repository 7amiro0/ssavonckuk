word = 'txt word init hello bro nine four samir nikita artem roma andrey lox'
key = input('enter your key')
key = key.split(",")
keys = []

for number in key:
    if int(number) < 0:
        keys.append('-1')
    else:
        keys.append('0')
    key = key.pop('-')

win = set()
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

for z in list1[::int(keys[0])]:
    for x in list2[::int(keys[1])]:
        for c in list3[::int(keys[2])]:
            for v in list4:
                if z not in win:
                    win.add(z)
                    win.add(x)
                    win.add(c)
                    win.add(v)

print(win)
