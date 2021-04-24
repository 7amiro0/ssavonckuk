"""Module for search palindromes."""
import urllib.request
import time


def main(args=''):
    """Hello text.

    :param args : command line arguments
    """
    start_time = time.time()

    my_file = open("kz.txt", 'w')

    with urllib.request.urlopen('https://greenteapress.com/thinkpython2/code/words.txt') as resp:
        sulka_one = resp.read().decode('utf-8').lower()

    with urllib.request.urlopen('https://inventwithpython.com/dictionary.txt') as resp:
        sulka_two = resp.read().decode('utf-8').lower()

    list_polegram = set(sulka_one.split() + sulka_two.split())
    list_polegramas = list()

    for runer in list_polegram:
        if runer == runer[::-1]:
            list_polegramas.append(runer)
            my_file.write(str(runer))
            my_file.write('\n')

    my_file.close()
    finish_time = time.time()

    print(__name__ == 'assigment1_part1.py')
    print('I was able to find ', str(len(list_polegramas)))
    print('I was able to do it for ', int(finish_time - start_time), 'sec')
    return args


if __name__ == '__main__':
    main()
