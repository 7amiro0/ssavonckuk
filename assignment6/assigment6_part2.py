"""Hi, my program can decrypt texts."""
"""Hi, my program can encrypt texts."""
"""Zigzag text encryption method."""
"""Example 'HBOOAEOIRHWRYU' turns into
HIBROHOWAREYOU"""

words = """Here you see your text that you want to decrypt."""

"""After this #=============#, do not touch or change anything."""
# ======================================================================================================================#

words = words.split() #<- text no have space
big_word = ''.join(words)

split = int(len(big_word) / 2)

more_later = [[], []]
resoult = ''

for later in big_word[:split:]: #<- first later in text
    more_later[0].append(later)

for later in big_word[split:]: #<- second later in text
    more_later[1].append(later)

for i in range(len(more_later[0])): #<- inserts letters at their positions
    resoult += ''.join(more_later[0][i])
    resoult += ''.join(more_later[1][i])

"""And here is the (not ideal) decryption of tex. """

print(resoult)

"""The end."""
