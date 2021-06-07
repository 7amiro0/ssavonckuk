"""After # ----------- # do not touch anything"""
"""Here is the text to be encrypted
                   |
                   V"""
words = "your text pleas"
#----------------------------------------------------------------------------------------------------------------------#

words = words.split()
big_word = ''.join(words)
split = int(len(big_word) / 3)

first_later = []
second_later = []
third_later = []
resoult = ''

for later in big_word[:split:]:
    first_later.append(later)

for later in big_word[split:split + split]:
    second_later.append(later)

for later in big_word[split + split:]:
    third_later.append(later)
all_list = [first_later, second_later, third_later]
print(all_list)
for i in range(len(first_later)):
    resoult += ''.join(all_list[0][i])
    resoult += ''.join(all_list[1][i])
    resoult += ''.join(all_list[2][i])
"""outputs the result
    |
    V"""
print(resoult)
