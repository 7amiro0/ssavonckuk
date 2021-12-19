"""Hi, my program can encrypt texts."""
"""Zigzag text encryption method."""
"""Example 'hi bro how are you' turns into
HBOOAEOIRHWRYU"""

words = """Here you see your text that you want to decrypt."""

"""After this #========#, do not touch or change anything."""
# ======================================================================================================================#

words = words.upper() #<- text no have space
words = words.split()
big_word = ''.join(words)

more_later = [[], []]
result = ''
space_in_txt = []

for later in big_word[::2]: #<- first later in text
    more_later.append(later)

for later in big_word[1::2]: #<- first later in text
    more_later.append(later)

for later in more_later[0] + more_later[1]: #<- replase letters at their positions
    space_in_txt.append(later)
for i in range(len(space_in_txt)):
    if (i + 1) % 5 == 0:
        space_in_txt.insert(i, ' ')
result += ''.join(space_in_txt)

print(result)

"""The end."""
