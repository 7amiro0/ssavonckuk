"""we have to write to file."""


def write(list_words, name_file):
    """But also create it."""
    my_file = open(name_file, 'w')

    for word in list_words:
        my_file.write(str(word) + '\n')
    my_file.close()
