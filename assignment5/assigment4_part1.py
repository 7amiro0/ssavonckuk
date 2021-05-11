from collections import defaultdict
word = 'txt word init hello bro nine four samir'
win = []
list_ = defaultdict(list)
for w in word.split():
    if len(list_[1]) < 5:
        list_[1].append(w)
        if len(list_[1]) > 5:
            list_[2].append(w)
print(list_)




