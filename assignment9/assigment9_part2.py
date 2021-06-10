import urllib.request

enter_text = """Panelateastendofchapelslides"""
enter_password = int(input("Enter here numbers later in word: "))
secrate = ''
point = 0
true_slovari = []

with urllib.request.urlopen('https://greenteapress.com/thinkpython2/code/words.txt') as resp:
    slovarif = resp.read().decode('utf-8').lower().split()

for slovof in range(len(slovarif)):
    if len(slovarif[slovof]) >= enter_password:
        true_slovari.append(slovarif[slovof])

slovo = true_slovari[point]

for x in enter_text:
    while slovo[enter_password - 1] != x.lower():
        point += 1
        slovo = true_slovari[point % len(true_slovari)]
        print(slovo, x)
    secrate += ' ' + slovo

print(secrate)
