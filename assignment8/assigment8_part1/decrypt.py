"""After # ----------- # do not touch anything"""
"""Here is the text to be encrypted"""
words = "your text pleas"
#----------------------------------------------------------------------------------------------------------------------#

"""text no have space"""
words = words.split()
big_word = ''.join(words)

split = int(len(big_word) / 3)

more_later = [[], [], []]
resoult = ''

"""first later in text"""
for later in big_word[:split:]:
    more_later[0].append(later)

"""second later in text"""
for later in big_word[split:split + split]:
    more_later[1].append(later)

"""third later in text"""
for later in big_word[split + split:]:
    more_later[2].append(later)

"""inserts letters at their positions"""
for i in range(len(more_later[0])):
    resoult += ''.join(more_later[0][i])
    resoult += ''.join(more_later[1][i])
    resoult += ''.join(more_later[2][i])

"""outputs the result"""
print(resoult)
