"""After # ----------- # do not touch anything"""
"""Here is the text to be encrypted
                   |
                   V"""
words = "your text pleas"
#----------------------------------------------------------------------------------------------------------------------#

words = words.split()
big_word = ''.join(words)
split = int(len(big_word) / 3)

more_later = [[], [], []]
resoult = ''

for later in big_word[:split:]:
    more_later[0].append(later)

for later in big_word[split:split + split]:
    more_later[1].append(later)

for later in big_word[split + split:]:
    more_later[2].append(later)
all_list = [more_later[0], more_later[1], more_later[2]]

for i in range(len(more_later[0])):
    resoult += ''.join(all_list[0][i])
    resoult += ''.join(all_list[1][i])
    resoult += ''.join(all_list[2][i])
"""outputs the result
    |
    V"""
print(resoult)
