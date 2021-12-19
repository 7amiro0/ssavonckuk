"""Module for search palindromes."""
import urllib.request
import time
from writer import write


def main():
    """in the function we have to do all the tasks."""
    start_time = time.time()

    with urllib.request.urlopen('https://greenteapress.com/thinkpython2/code/words.txt') as resp:
        link_one = resp.read().decode('utf-8').lower()

    with urllib.request.urlopen('https://inventwithpython.com/dictionary.txt') as resp:
        link_two = resp.read().decode('utf-8').lower()

    list_words = set(link_one.split() + link_two.split())

    list_palindrome = []

    for word in list_words:
        if word == word[::-1]:
            list_palindrome.append(word)

    write(list_palindrome, "file.txt")
    duration_program = time.time() - start_time
    print("duration program =", duration_program, "found palindrome", len(list_palindrome))


if __name__ == '__main__':
    main()
