"""Home works."""
import urllib.request
import cProfile


def main():
    """Works function."""
    with urllib.request.urlopen('https://inventwithpython.com/dictionary.txt') as resp:
        link = set(resp.read().decode('utf-8').lower().split())

    word_list = []

    for word in link:
        if word[::-1] in link:
            word_list.append(word)
        if word[1::-1] in link:
            word_list.append(word)
        if word[2::-1] in link:
            word_list.append(word)
        if word[3::-1] in link:
            word_list.append(word)
        if word[4::-1] in link:
            word_list.append(word)
        if word[5::-1] in link:
            word_list.append(word)
        if word[6::-1] in link:
            word_list.append(word)
        if word[7::-1] in link:
            word_list.append(word)

    my_file = open('record.txt', 'w')
    word_list.sort()
    for word in set(word_list):
        my_file.write(str(word) + '\n')

    my_file.close()


main()
cProfile.run('main()')
