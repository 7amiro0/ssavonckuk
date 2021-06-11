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
    true_slovari = []
    text = text.lower()

    with urllib.request.urlopen("https://greenteapress.com/" \
                                "thinkpython2/code/words.txt") as resp:
        slovarif = resp.read().decode('utf-8').lower().split()

    for word in slovarif:
        if len(word) >= key:
            true_slovari.append(word)

    if key > len(true_slovari):
        print('Your key very big')
        exit()

    slovo = true_slovari[point]

    for later in text:
        while slovo[key - 1] != later:
            point += 1
            slovo = true_slovari[point % len(true_slovari)]
        secrate += ' ' + slovo

    print(secrate)


if __name__ == "__main__":
    main(TEXT, KEY)
