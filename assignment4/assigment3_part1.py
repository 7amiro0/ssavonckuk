"""Home work number 4."""
from collections import defaultdict
import urllib.request
import cProfile


def main():
    """Works function."""
    with urllib.request.urlopen('https://inventwithpython.com/dictionary.txt') as resp:
        link1 = resp.read().decode('utf-8').lower().split()
    with urllib.request.urlopen('https://greenteapress.com/thinkpython2/code/words.txt') as resp:
        link2 = resp.read().decode('utf-8').lower().split()
    with urllib.request.urlopen('http://www-personal.umich.edu/~jlawler/wordlist') as resp:
        link3 = resp.read().decode('utf-8').lower().split()

    dict_ = defaultdict(set)

    while 1:
        enter = input('enter your anegrame: ')
        enter_sort = ''.join(sorted(enter))

        if len(enter) > 1:

            for word in link1:
                if enter_sort == ''.join(sorted(word)) and enter != word:
                    dict_[enter].add(word)

            for word in link2:
                if enter_sort == ''.join(sorted(word)) and enter != word:
                    dict_[enter].add(word)

            for word in link3:
                if enter_sort == ''.join(sorted(word)) and enter != word:
                    dict_[enter].add(word)

            if len(dict_) == 0:
                print('no anagram found for word ')
            else:
                print(dict_)


cProfile.run('main()')
