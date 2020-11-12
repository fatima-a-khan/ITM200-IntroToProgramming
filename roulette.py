# roulette.py
# Author: Fatima Khan 500766544
import random

listSize = int(input("(Player) Enter the size of list: \n"))

list = [None] * listSize

for i in range(listSize):
    list[i] = random.randint(0, 10)

print('Original list: *DEBUGGING PURPOSES*', list)


while True:
    inp = int(input("(Player) Enter your guess: \n"))

    if inp == list[0]:
        print('(Player) You Win!')
        break
    list.insert (0, list.pop(listSize-1))
    print('Current list: *DEBUGGING PURPOSES*', list)









