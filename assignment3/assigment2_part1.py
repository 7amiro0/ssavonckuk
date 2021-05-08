"""Home works."""
import urllib.request
import cProfile


def main():
    """Works function."""
    with urllib.request.urlopen('https://inventwithpython.com/dictionary.txt') as resp:
        link = set(resp.read().decode('utf-8').lower().split())
    word_list = []

    for word in link:
        rever_word = word[::-1]
        for len_ in range(0, len(word)):
            if word[len_:] in word_list or word[len_:] == word[len_::-1]:
                if len_ != len(word):
                    word_list.append(word)
                    word_list.append(rever_word)
                continue
            if rever_word[len_:] in word_list or rever_word[len_:] == rever_word[len_::-1]:
                if len_ != len(word):
                    word_list.append(word)
                    word_list.append(rever_word)
    my_file = open('record.txt', 'w')
    word_list.sort()
    for word in set(word_list):
        my_file.write(str(word) + '\n')

    my_file.close()


main()
cProfile.run('main()')
