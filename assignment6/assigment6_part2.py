"""Hi, my program can decrypt texts."""
"""Hi, my program can encrypt texts."""
"""Zigzag text encryption method."""
"""Example 'HBOOAEOIRHWRYU' turns into
HIBROHOWAREYOU"""

words = """Here you see your text that you want to decrypt."""

"""After this #=============#, do not touch or change anything."""
# ======================================================================================================================#

"""text no have space
        |
        V"""
words = words.split()
big_word = ''.join(words)

split = int(len(big_word) / 2)

more_later = [[], []]
resoult = ''

"""first later in text
        |
        V"""
for later in big_word[:split:]:
    more_later[0].append(later)

"""second later in text
        |
        V"""
for later in big_word[split:]:
    more_later[1].append(later)

"""inserts letters at their positions
            |
            V"""
for i in range(len(more_later[0])):
    resoult += ''.join(more_later[0][i])
    resoult += ''.join(more_later[1][i])

"""And here is the (not ideal) decryption of tex. """

print(resoult)

"""The end."""
