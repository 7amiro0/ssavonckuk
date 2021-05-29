"""Hi, my program can encrypt texts."""
"""Zigzag text encryption method."""
"""Example 'hi bro how are you' turns into
HBOOAEOIRHWRYU"""

words = """Here you see your text that you want to decrypt."""

"""After this #========#, do not touch or change anything."""
# ======================================================================================================================#

words = words.upper()
words = words.split()
big_word = ''.join(words)

first_later = []
second_later = []
resoult = ''
space_in_txt = []

for later in big_word[::2]:
    first_later.append(later)

for later in big_word[1::2]:
    second_later.append(later)

for later in first_later + second_later:
    space_in_txt.append(later)
for i in range(len(space_in_txt)):
    if (i + 1) % 5 == 0:
        space_in_txt.insert(i, ' ')
resoult += ''.join(space_in_txt)

print(resoult)

"""The end."""
