# Divyansh Goyal's Mini Word Scramble Game

import math
import time
import random
import colorama
from colorama import Fore, Back, Style
colorama.init()

start = time.time()
# Intro.
print("This is a game where you have 5 scrambled words which you need to unscramble, in the end, you will receive a score out of 5. \n . \n . \n .")

score = 0
input1 = ""
measure = True

# Word Banks for each level.
six_letter_word_bank = ["invest", "debate", "family", "global",
                        "leader", "normal", "obtain", "nearly", "played", "school"]
first = six_letter_word_bank[random.randint(0, 9)]

seven_letter_word_bank = ["ability", "courage", "awesome",
                          "element", "learned", "mission", "prepare", "section", "working", "booking"]
second = seven_letter_word_bank[random.randint(0, 9)]

eight_letter_word_bank = ["achieved", "champion", "hardware", "purposes",
                          "websites", "advisory", "explorer", "premises", "workflow", "airports"]
third = eight_letter_word_bank[random.randint(0, 9)]

nine_letter_word_bank = ["batteries", "different", "liability", "addiction",
                         "instances", "residence", "bandwidth", "directing", "ignorance", "ministers"]
fourth = nine_letter_word_bank[random.randint(0, 9)]

ten_letter_word_bank = ["functional", "connection", "accounting", "physicians",
                        "brightness", "disconnect", "renovation", "cafeterias", "delicacies", "vegetarian"]
fifth = ten_letter_word_bank[random.randint(0, 9)]


# Checks whether input in correct or incorrect and displays message accordingly.
def scramble(a):
    input1 = input("Enter Answer: ")
    count = 0
    while input1.lower() != a.lower():
        input1 = input("Try Again: ")
        count += 1
        if count > 1 and input1.lower() != a.lower():
            count = 0
            return Fore.RED + "Incorrect! \nCorrect Answer is: " + a + " \n . \n . \n . " + Style.RESET_ALL
    if input1.lower() == a.lower():
        global score
        score += 1
        return Fore.GREEN + "Well Done! Next Level \n . \n . \n ." + Style.RESET_ALL


# Takes the word and scrambles it a unique way each time the game is played.
def scrambler(a):
    l = []
    length = len(a)
    randomnum = random.sample(range(length), length)
    for i in range(length):
        l.append(a[randomnum[i]].lower())
    print(l)


# Level One
print("This is Level One: ")
scrambler(first)
print(scramble(first))

# Level Two
print("This is Level Two")
scrambler(second)
print(scramble(second))

# Level Three
print("This is Level Three")
scrambler(third)
print(scramble(third))

# Level Four
print("This is Level Four")
scrambler(fourth)
print(scramble(fourth))

# Level Five
print("This is Level Five")
scrambler(fifth)
print(scramble(fifth))

# Conclusion Screen
print("\n . \n . \n .")
if score >= 2:
    print(Back.BLACK + Fore.GREEN + "The game has concluded, your score is:" +
          " " + str(score) + "/5!" + Style.RESET_ALL)
else:
    print(Back.BLACK + Fore.RED + "The game has concluded, your score is:" +
          " " + str(score) + "/5!" + Style.RESET_ALL)

time = (time.time() - start)
seconds = math.modf(time)

if time <= 60.00:
    print("You played this game for about",
          round(time, 2), "seconds")
else:
    print(
        f"You played this game for about {int(time/60)}: {int((seconds[0]*60))} minutes")
