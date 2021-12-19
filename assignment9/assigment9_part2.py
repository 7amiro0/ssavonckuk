"""After # ----------- # do not touch anything."""
"""This program masks 0 slate as plain text"""

import urllib.request

"""Here secrate text masks 0 slate as plain text."""
TEXT = """Panelateastendofchapelslides"""

"""Here, what letter should it go"""
KEY = 3  # here we enter your password


# -------------------------------------------------------------------------------------------------------------------- #
def main(text, key):
    """Work function encrypt."""
    secrate = ''
    point = 0
    dictionary = []
    text = text.lower()

    with urllib.request.urlopen("https://greenteapress.com/" \
                                "thinkpython2/code/words.txt") as resp:
        dictionary_words = resp.read().decode('utf-8').lower().split()

    for word in dictionary_words:
        if len(word) >= key:
            dictionary.append(word)

    if key > 13:
        print('The key is too huge')
        exit()

    word = dictionary[point]

    for later in text:
        while word[key - 1] != later:
            point += 1
            word = dictionary[point % len(dictionary)]
        secrate += ' ' + word

    print(secrate)


if __name__ == "__main__":
    main(TEXT, KEY)
