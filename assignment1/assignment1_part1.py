import urllib.request
import time

start_time = time.time()

my_file = open("kz.txt", 'w')

with urllib.request.urlopen('https://greenteapress.com/thinkpython2/code/words.txt') as resp:
    sulka_one = resp.read().decode('utf-8').lower()

with urllib.request.urlopen('https://inventwithpython.com/dictionary.txt') as resp:
    sulka_two = resp.read().decode('utf-8').lower()

list_polegram = set(sulka_one.split() + sulka_two.split())
list_polegramas = list()

for x in list_polegram:
    if x == x[::-1]:
        list_polegramas.append(x)
        my_file.write(str(x))
        my_file.write('\n')

my_file.close()

finish_time = time.time()

print('I was able to find ', str(len(list_polegramas)))
print('I was able to do it for ', int(finish_time - start_time), 'sec')
