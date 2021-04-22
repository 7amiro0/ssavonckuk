import urllib.request
import time
from pprint import *

start_time = time.time()

my_file = open("kz.txt", 'w')

with urllib.request.urlopen('https://greenteapress.com/thinkpython2/code/words.txt') as resp:
    sulka_one = resp.read().decode('utf-8')

with urllib.request.urlopen('https://inventwithpython.com/dictionary.txt') as resp:
    sulka_two = resp.read().decode('utf-8')

l = sulka_one.split()
z = list()
l2 = sulka_two.split()

for x in l:
    if x == x[::-1]:
        if x in z:
            pass
        else:
            z.append(x)
            my_file.write(str(x))
            my_file.write('\n')

for x in l2:
    if x == x[::-1]:
        if x in z:
            pass
        else:
            z.append(x)
            my_file.write(str(x))
            my_file.write('\n')

my_file.write(str(len(z)))
my_file.write(' ')
my_file.close()

finish_time = time.time()

print('sec', int(finish_time / 1000))