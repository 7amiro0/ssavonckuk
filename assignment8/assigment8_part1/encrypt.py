"""After # ----------- # do not touch anything"""
"""Here is the text to be encrypted"""
words = "your text pleas"
#----------------------------------------------------------------------------------------------------------------------#

"""text no have space"""
words = words.upper()
words = words.split()
big_word = ''.join(words)

more_later = [[], [], []]
resoult = ''
space_in_txt = []

"""first later in text"""
for later in big_word[::3]:
    more_later[0].append(later)

"""second later in text"""
for later in big_word[1::3]:
    more_later[1].append(later)

"""third later in text"""
for later in big_word[2::3]:
    more_later[2].append(later)

"""replase letters at their positions"""
for later in more_later[0] + more_later[1] + more_later[2]:
    space_in_txt.append(later)
for i in range(len(space_in_txt)):
    if (i + 1) % 5 == 0:
        space_in_txt.insert(i, ' ')
resoult += ''.join(space_in_txt)

"""outputs the result"""
print(resoult)
