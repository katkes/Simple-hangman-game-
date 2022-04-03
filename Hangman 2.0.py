#word bank
words = ['hockey','house','queasy','jumped','backup','pencil','keshan','planet','brazil','jetski','influx','squeak','hazing','expand']

#word picking time

x = 0

import random

num = random.randint(0,14)

word = words[num]

#guessing system

wordletters = list(word)
display = []
for i in wordletters:
    display.append('_')

print(display)
tries = 8

while x == 0:
    guess = str(input("guess a letter!: "))

    if guess in wordletters:
        for i in wordletters:
            display[wordletters.index(guess)] = guess

        print(display)

    else:
        print("letter isn't in the word, try again!")
        tries -=1

    if display == wordletters:
        print('you win!')
        x = 5

    if tries == 0:
        print('you lost')
        cont = input("press e to exit: ")

        exit()  
        x = 5
