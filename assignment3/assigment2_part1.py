"""Home works."""
import urllib.request
import cProfile


def main():
    """Works function."""
    with urllib.request.urlopen('https://inventwithpython.com/dictionary.txt') as resp:
        link = set(resp.read().decode('utf-8').lower().split())

    word_list = []

    for rider in link:
        if rider == rider[::-1]:
            word_list.append(rider)
            word_list.sort()

    my_file = open('record.txt', 'w')

    for word in word_list:
        my_file.write(str(word) + '\n')

    my_file.close()


cProfile.run('main()')
