"""Hi, my program can decrypt texts."""
"""Hi, my program can encrypt texts."""
"""Zigzag text encryption method."""
"""Example 'HBOOAEOIRHWRYU' turns into
HIBROHOWAREYOU"""

words = """Here you see your text that you want to decrypt."""

"""After this #=============#, do not touch or change anything."""
# ======================================================================================================================#

words = words.split()
big_word = ''.join(words)
split = int(len(big_word) / 2)

first_later = []
second_later = []
resoult = ''

for later in big_word[:split:]:
    first_later.append(later)
for later in big_word[split:]:
    second_later.append(later)
all_list = [first_later, second_later]
for i in range(len(first_later)):
    resoult += ''.join(all_list[0][i])
    resoult += ''.join(all_list[1][i])

"""And here is the (not ideal) decryption of tex. """

print(resoult)

"""The end."""
