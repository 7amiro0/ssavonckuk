"""Home works."""
import urllib.request
import cProfile


def main():
    """Works function."""
    with urllib.request.urlopen('https://inventwithpython.com/dictionary.txt') as resp:
        link = set(resp.read().decode('utf-8').lower().split())

    word_list = set()

    for word in link:
        rever_word = word[::-1]

        for len_ in range(len(word)):
            if word[len_:] == word[len_:][::-1] and word[:len_:][::-1] in link:
                word_list.add(word + " " + word[:len_:][::-1])
            if rever_word[len_ + 1:] == rever_word[len_ + 1::][::-1] and rever_word[:len_ + 1:] in link:
                word_list.add(rever_word[:len_ + 1:] + " " + word)


    print(len(word_list))
    my_file = open('record.txt', 'w')

    for word in set(word_list):
        my_file.write(str(word) + '\n')
    my_file.close()


main()
cProfile.run('main()')
