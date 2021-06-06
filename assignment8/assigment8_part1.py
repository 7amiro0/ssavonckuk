"""After # ----------- # do not touch anything"""
"""Here is the text to be encrypted
                   |
                   V"""
words = "your text pleas"
#----------------------------------------------------------------------------------------------------------------------#
words = words.upper()
words = words.split()
big_word = ''.join(words)

first_later = []
second_later = []
third_later = []
resoult = ''
space_in_txt = []

for later in big_word[::3]:
    first_later.append(later)

for later in big_word[1::3]:
    second_later.append(later)

for later in big_word[2::3]:
    third_later.append(later)

for later in first_later + second_later + third_later:
    space_in_txt.append(later)
for i in range(len(space_in_txt)):
    if (i + 1) % 5 == 0:
        space_in_txt.insert(i, ' ')
resoult += ''.join(space_in_txt)

"""outputs the result
    |
    V"""
print(resoult)
