"""Hi, my program can encrypt texts."""
"""Zigzag text encryption method."""
"""Example 'hi bro how are you' turns into
HBOOAEOIRHWRYU"""

words = """Here you see your text that you want to decrypt."""

"""After this #========#, do not touch or change anything."""
# ======================================================================================================================#

"""text no have space
        |
        V"""
words = words.upper()
words = words.split()
big_word = ''.join(words)

more_later = [[], []]
result = ''
space_in_txt = []

"""first later in text
        |
        V"""
for later in big_word[::2]:
    more_later.append(later)

"""second later in text
        |
        V"""
for later in big_word[1::2]:
    more_later.append(later)

"""replase letters at their positions
            |
            V"""
for later in more_later[0] + more_later[1]:
    space_in_txt.append(later)
for i in range(len(space_in_txt)):
    if (i + 1) % 5 == 0:
        space_in_txt.insert(i, ' ')
result += ''.join(space_in_txt)

print(result)

"""The end."""
